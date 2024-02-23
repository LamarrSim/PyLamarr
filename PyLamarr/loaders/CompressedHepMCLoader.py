from typing import List
import shutil
import random
import os.path
from glob import glob
import tarfile
import logging
import re

from typing import Optional

class CompressedHepMCLoader:
    """
    Adapter to read HepMC2 files compressed in a tar file. Requires SQLamarr.
    """
    def __init__(self, 
            regexp_runNumber: str = "Run([0-9]+)",
            regexp_evtNumber: str = "evt([0-9]+)",
            tmpdir: str = "/tmp",
            max_event: Optional[int] = None,
            ):
        self.tmpdir = tmpdir
        self._db = None
        self._hepmcloader = None
        self._batch_counter = 0
        self._regexp_runNumber = regexp_runNumber
        self._regexp_evtNumber = regexp_evtNumber
        self._max_event = max_event
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


        runNumber = self._get_run_number(filename)

        event_counter = 0

        with self._db.connect() as c:
            for i_file, hepmc_file in enumerate(self.files_in_archive(filename)):
                evtNumber = self._get_evt_number(hepmc_file, i_file)
                self._hepmcloader.load(hepmc_file, runNumber, evtNumber)
                event_counter += 1
                if self._max_event is not None and event_counter >= self._max_event: 
                    break

