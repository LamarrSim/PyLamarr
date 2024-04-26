from typing import List
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
            logging.getLogger('HepMC2EventBatch').debug(f"Loading {hepmc_file}")
            self._hepmcloader.load(hepmc_file, run_number, event_number)



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

    def files_in_archive(self, filename: str):
        tmp_dir = os.path.join(
            self.tmpdir, 
            f"pylamarr.tmp.{random.randint(0, 0xFFFFFF):06x}"
            )
        os.mkdir(tmp_dir)
        tmp_archive = f"{tmp_dir}.tar.bz2"

        try:
            self.logger.info(f"Copying archive to local storage")
            shutil.copy(filename, tmp_archive)
            self.logger.info(f"Extracting archive {filename} in {tmp_dir}")
            with tarfile.open(tmp_archive) as archive:
                archive.extractall(tmp_dir)

#            for filename in glob(os.path.join(tmp_dir, '*')):
#                yield filename
            for (root, dirs, filenames) in os.walk(tmp_dir):
                for filename in filenames:
                    if filename.endswith(".mc2"):
                        yield os.path.join(root, filename)

        finally:
            self.logger.info(f"Removing directory {tmp_dir}")
            shutil.rmtree(tmp_dir)
            self.logger.info(f"Removing temporary file {tmp_archive}")
            os.remove(tmp_archive)


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
        for i_file, hepmc_file in enumerate(self.files_in_archive(filename)):
            run_number = self._get_run_number(filename) 
            event_number = self._get_evt_number(hepmc_file, i_file)
            n_events = len(batches['event_numbers'])
            batch_info = dict(
                n_events=n_events,
                batch_id=batch_counter,
                description=f"Run {run_number}", 
                _hepmcloader=self._hepmcloader,
            )
            
            if tot_events > 0:
                batch_info['n_batches'] = ceil(tot_events/self._events_per_batch) 

            if self._max_event is not None and event_counter >= self._max_event: 
                yield HepMC2EventBatch(
                    **batch_info,
                    **batches
                    )
                batch_counter += 1
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


