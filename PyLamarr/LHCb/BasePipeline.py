import xml.etree.ElementTree as e3
import os
import itertools
import PyLamarr
import logging
import sys
import threading
import sqlite3
from PyLamarr import GenericWrapper
from PyLamarr.RemoteResource import RemoteResource as RemoteRes

from typing import List, Tuple, Any, Union, Dict


class BasePipeline:
    def __init__(self,
                 sequence: Union[List[Tuple[Any]], None] = None,
                 loader: str = "HepMC2DataLoader",
                 batch=1,
                 dbfile_fmt="file:/tmp/lamarr.{thread:016x}.db?cache=shared",
                 clean_before_loading=True,
                 clean_after_finishing=True,
                 ):
        self.logger = logging.getLogger(self.__class__.__name__)
        PyLamarr.configure_logger()
        self.logger.info(f"Python {sys.version}".replace("\n", " "))

        with sqlite3.connect(":memory:") as c:
            sqlite_version = c.execute("SELECT sqlite_version()").fetchall()[0][0]
        self.logger.info(f"Running with SQLite version {sqlite_version} "
                         f"(bindings: {sqlite3.version})")

        try:
            import SQLamarr
        except (ImportError, OSError):
            self._sqlamarr_available = False
            self.logger.warning(f"SQLite not found. "
                                "You can still build a configuration, but not run it.")
        else:
            self._sqlamarr_available = True
            self.logger.info(f"Running with SQLamarr version {SQLamarr.version}")

        self._sequence = sequence if sequence is not None else self.default_sequence
        self._loader = loader
        self._batch = batch
        self._dbfile_fmt = dbfile_fmt
        self._clean_before_loading = clean_before_loading
        self._clean_after_finishing = clean_after_finishing

    @property
    def default_sequence(self):
        return []

    @property
    def sequence(self):
        return self._sequence

    @property
    def loader(self):
        if isinstance(self._loader, str) and self._sqlamarr_available:
            import SQLamarr
            return getattr(SQLamarr, self._loader)
        return self._loader

    @property
    def batch(self):
        return self._batch

    @loader.setter
    def loader(self, new_loader):
        self._loader = new_loader

    @batch.setter
    def batch(self, new_batch):
        self._batch = new_batch

    @staticmethod
    def _batched(batch, batch_size):
        if batch_size < 1:
            raise ValueError("Batch size must be larger than 1")

        it = iter(batch)
        while True:
            batch = tuple(itertools.islice(it, batch_size))
            if batch:
                yield batch
            else:
                break

    def execute(self,
                load_args: List[Tuple[Dict]],
                thread_id: Union[int, None] = None
                ):
        if not self._sqlamarr_available:
            raise ImportError("SQLite is needed for pipeline.execute(). "
                              "Please reinstall as `pip install PyLamarr[SQLamarr]`")

        import SQLamarr

        tid = thread_id if thread_id is not None else threading.get_ident()
        # FIXME: inmemory DB is not working here...
        # db = SQLamarr.SQLite3DB(f"file:memdb{tid}?mode=memory&cache=shared")
        parsed_fmt = self._dbfile_fmt.format(thread=tid)
        self.logger.info(f"Connecting to SQLite db: {parsed_fmt}")
        db = SQLamarr.SQLite3DB(parsed_fmt)
        db.seed(tid)
        loader = self.loader(db)

        clean = SQLamarr.Pipeline([SQLamarr.CleanEventStore(db)])

        pipeline = SQLamarr.Pipeline([
            make_algo(db) for _, make_algo in self.sequence
        ])

        self.logger.info(f"Algorithms:")
        for iAlg, (name, _) in enumerate(self.sequence, 1):
          self.logger.info(f"  {iAlg:>2d}. {name}")

        for batch in self._batched(load_args, self.batch):
            if self._clean_before_loading:
                self.logger.debug("Cleaning database")
                clean.execute()
            else:
                self.logger.debug("Cleaning database was DISABLED")

            for load_arg in batch:
                self.logger.info(f"Loading {load_arg}")
                if isinstance(load_arg, (list, tuple)):
                    loader.load(*load_arg)
                elif isinstance(load_arg, (dict,)):
                    loader.load(**load_arg)
                else:
                    loader.load(load_arg)

            self.logger.debug(f"Executing pipeline on a batch of {len(batch)}")
            pipeline.execute()

        if self._clean_after_finishing:
            if parsed_fmt.startswith("file:"):
                if "mode=memory" not in parsed_fmt:
                    if '?' in parsed_fmt:
                        os.remove(parsed_fmt[len('file:'):parsed_fmt.index('?')])
                    else:
                        os.remove(parsed_fmt[len('file:'):])
            else:
                os.remove(parsed_fmt)


    def to_xml(self, file_like) -> None:
        root = e3.Element("pipeline", batch=str(self.batch))

        for k, w in self.sequence:
            if hasattr(w, 'to_xml'):
                w.to_xml(root).attrib['step'] = k
            else:
                self.logger.warning(f"XML serialization unavailable for {k}. Skipped.")

        file_like.write(e3.tostring(root, encoding='unicode'))

    @classmethod
    def read_xml(cls, file_like):
        root = e3.fromstring(file_like.read())
        if root.tag.lower() not in ['pipeline']:
            raise IOError(f"Unexpected ROOT tag {root.tag}")

        batch_size = int(root.attrib.get("batch", 1))

        algs = []
        for child in root:
            alg_type = child.tag
            alg_name = child.attrib.get("name", alg_type)
            step_name = child.attrib.get('step', alg_name)
            config = dict()
            for cfg_node in child:
                if cfg_node.tag.lower() == "config":
                    if cfg_node.attrib['type'] == 'str':
                        config[cfg_node.attrib['key']] = cfg_node.text
                    elif cfg_node.attrib['type'] == 'seq':
                        config[cfg_node.attrib['key']] = cfg_node.text.split(";")
                    elif cfg_node.attrib['type'] == 'url':
                        config[cfg_node.attrib['key']] = RemoteRes(cfg_node.text)
                    else:
                        raise NotImplementedError(
                            f"Unexpected type {cfg_node.attrib['type']} for {cfg_node.attrib['key']}"
                            )

            algs.append((step_name, GenericWrapper(implements=alg_type, config=config)))

        return cls(algs, batch=batch_size)
