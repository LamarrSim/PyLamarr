from typing import List
from contextlib import contextmanager
from math import ceil
import shutil
import random
import os.path
from glob import glob
from dataclasses import dataclass
import tarfile
import logging
import re

from typing import Optional, Collection, Any

from pkg_resources import require

from PyLamarr import EventBatch

@dataclass
class HepMC2EventBatch (EventBatch):
    _hepmcloader: Any = None # Expected SQLamarr.HepMC2DataLoader not explicit for optional SQLamarr dep
    input_files: Collection[str] = None
    run_numbers: Collection[int] = None
    event_numbers: Collection[int] = None

    def load(self):
        files_runs_events = zip(self.input_files, self.run_numbers, self.event_numbers)
        for hepmc_file, run_number, event_number in files_runs_events:
            logging.getLogger('HepMC2EventBatch').debug(f"Loading file {hepmc_file}")
            self._hepmcloader.load(hepmc_file, run_number, event_number)
            logging.getLogger("HepMC2EventBatch").debug("Loaded.")

class CompressedHepMCLoader:
    """
    Adapter to read HepMC2 files compressed in a tar file. Requires SQLamarr.
    """
    def __init__(self, 
            regexp_runNumber: str = "Run([0-9]+)",
            regexp_evtNumber: str = "evt([0-9]+)",
            regexp_totEvents: str = "([0-9]+)ev[^\w]",
            tmpdir: str = "/tmp",
            max_event: Optional[int] = None,
            events_per_batch: Optional[int] = None,
            ):
        self.tmpdir = tmpdir
        self._db = None
        self._hepmcloader = None
        self._batch_counter = 0
        self._regexp_runNumber = regexp_runNumber
        self._regexp_evtNumber = regexp_evtNumber
        self._regexp_totEvents = regexp_totEvents
        self._max_event = max_event
        self._events_per_batch = events_per_batch
        self._particle_gun_patched_events = 0
        self.logger = logging.getLogger("CompressedHepMCLoad")

    def __call__(self, database):
        import SQLamarr
        self._db = database
        self._hepmcloader = SQLamarr.HepMC2DataLoader(database)
        return self

    def _get_run_number(self, filename) -> int:
        matches = re.findall(self._regexp_runNumber, filename)
        if len(matches) > 0:
            self._batch_counter = matches[-1]
        else:
            self._batch_counter += 1

        return int(self._batch_counter)

    def _get_evt_number(self, filename: str, default: int) -> int:
        matches = re.findall(self._regexp_evtNumber, filename)
        return int(matches[-1]) if len(matches) else default

    def _get_number_of_events(self, filename: str, default: int) -> int:
        matches = re.findall(self._regexp_totEvents, filename)
        return int(matches[-1]) if len(matches) else default


    @contextmanager
    def archive_mirror(self, filename: str):
        tmp_dir = os.path.join(
            self.tmpdir, 
            f"pylamarr.tmp.{random.randint(0, 0xFFFFFF):06x}"
            )
        os.mkdir(tmp_dir)
        tmp_archive = f"{tmp_dir}.tar.bz2"

        try:
            yield self.files_in_archive(filename, tmp_dir=tmp_dir, tmp_archive=tmp_archive)
        finally:
            self.logger.info(f"Removing directory {tmp_dir}")
            shutil.rmtree(tmp_dir)
            self.logger.info(f"Removing temporary file {tmp_archive}")
            os.remove(tmp_archive)

    def copy_and_maybe_patch_hepmc(self, filename):
        "Apply patches to the HepMC2 file to avoid segmentation fault in HepMC3 ascii reader"
        requires_particle_gun_patch = False
        with open(filename) as input_file:
            lines = []
            for line in input_file:
                line = line[:-1] if line[-1] == '\n' else line
                if len(line) > 0 and line[0] == 'E': ## Event line
                    tokens = line.split(" ")
                    # Documentation at https://hepmc.web.cern.ch/hepmc/releases/HepMC2_user_manual.pdf
                    # Section 6.2
                    if int(tokens[6]) == 1:  # For Particle Gun process
                        self._particle_gun_patched_events += 1
                        n_vertices = int(tokens[8])
                        tokens[8] = str(n_vertices + 1)
                        tokens[12 + int(tokens[11])] = str(1)
                        tokens += ["1.0"]
                        requires_particle_gun_patch = True
                        lines += [" ".join(tokens), 'N 1 "0"']
                    else:
                        lines.append(line)
                elif len(line) > 0 and line[0] == 'V' and requires_particle_gun_patch: # First vertex
                    # PGUN Patch:
                    # HepMC3::HepMC2Reader does not tolerate a PV with no incoming particles,
                    # so we create a fake vertex and a fake beam particle.
                    vertex_id = line.split(" ")[1]
                    lines += ["V -99999 0 0 0 0 0 0 0 0", "P 0 0 0. 0. 0. 0. 0. 3 0 0 %s 0" % vertex_id, line]
                    requires_particle_gun_patch = False
                else:
                    lines.append(line)

            return "\n".join(lines)
        
    def files_in_archive(self, filename: str, tmp_dir: str, tmp_archive: str):
        self.logger.info(f"Copying archive to local storage")
        shutil.copy(filename, tmp_archive)
        self.logger.info(f"Extracting archive {filename} in {tmp_dir}")
        with tarfile.open(tmp_archive) as archive:
            archive.extractall(tmp_dir)

        for (root, dirs, filenames) in os.walk(tmp_dir):
            for filename in filenames:
                if filename.endswith(".mc2"):
                    self.logger.info(f"Found {filename} in archive.")
                    with open(os.path.join(tmp_dir, filename), 'w') as file_copy:
                        file_copy.write(self.copy_and_maybe_patch_hepmc(os.path.join(root, filename)))
                    yield os.path.join(tmp_dir, filename)



    def load(self, filename: str):
        """
        Internal. 
        """
        if self._db is None:
            raise ValueError("PandasLoader tried loading with uninitialized db.\n"
                    "Missed ()?")

        event_counter = 0
        batch_counter = 0
        tot_events = min(
            self._get_number_of_events(filename, -1), 
            self._max_event if self._max_event is not None else 0x7FFFFFFF
            )

        batches = {k: [] for k in ('input_files', 'run_numbers', 'event_numbers')}
        batch_info = dict()
        with self.archive_mirror(filename) as files_in_archive:
            for i_file, hepmc_file in enumerate(files_in_archive):
                run_number = self._get_run_number(filename) 
                event_number = self._get_evt_number(hepmc_file, i_file)
                n_events = len(batches['event_numbers'])
                batch_info.update(dict(
                    n_events=n_events,
                    batch_id=batch_counter,
                    description=f"Run {run_number}", 
                    _hepmcloader=self._hepmcloader,
                ))
                
                if tot_events > 0 and self._events_per_batch is not None:
                    batch_info['n_batches'] = ceil(tot_events/self._events_per_batch) 

                if self._max_event is not None and event_counter >= self._max_event: 
                    break

                if self._events_per_batch is not None and n_events >= self._events_per_batch: 
                    yield HepMC2EventBatch(
                        **batch_info,
                        **batches
                        )
                    batches = {k: [] for k in batches.keys()}
                    batch_counter += 1


                batches['input_files'].append(hepmc_file)
                batches['run_numbers'].append(run_number)
                batches['event_numbers'].append(event_number)
                event_counter += 1

        if self._particle_gun_patched_events > 0:
            self.logger.warning(
                f"{self._particle_gun_patched_events} / {event_counter} events were identified as generated with a "
                "Particle Gun and patched."
            )


