import SQLamarr
import itertools
import PyLamarr
import logging 
import sys
import threading 
import sqlite3

from typing import List, Tuple, Any, Union, Dict

class BasePipeline:
  def __init__ (self, 
      sequence: Union[List[Tuple[Any]], None] = None, 
      loader=SQLamarr.HepMC2DataLoader,
      batch=1,
      dbfile_fmt="file:/tmp/lamarr.{thread:016x}.db?cache=shared",
      clean_before_loading=True,
      ):
    self.logger = logging.getLogger(self.__class__.__name__)
    PyLamarr.configure_logger()
    self.logger.info(f"Python {sys.version}".replace("\n", " "))
    self.logger.info(f"Running with SQLamarr version {SQLamarr.version}")
    with sqlite3.connect(":memory:") as c:
      sqlite_version = c.execute("SELECT sqlite_version()").fetchall()[0][0]
    self.logger.info(f"Running with SQLite version {sqlite_version} "
        f"(bindings: {sqlite3.version})")

    self._sequence = sequence if sequence is not None else self.default_sequence
    self._loader = loader
    self._batch = batch
    self._dbfile_fmt = dbfile_fmt
    self._clean_before_loading = clean_before_loading

    

  @property
  def default_sequence(self):
    return [

        ]

  @property 
  def sequence (self):
    return self._sequence

  @property 
  def loader (self):
    return self._loader

  @property 
  def batch (self):
    return self._batch

  @loader.setter
  def loader (self, new_loader):
    self._loader = new_loader

  @batch.setter
  def batch (self, new_batch):
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
      thread_id: Union[int,None] = None
      ):
    tid = thread_id if thread_id is not None else threading.get_ident()  
    # FIXME: inmemory DB is not working here...
    #db = SQLamarr.SQLite3DB(f"file:memdb{tid}?mode=memory&cache=shared")
    parsed_fmt = self._dbfile_fmt.format(thread=tid)
    self.logger.info(f"Connecting to SQLite db: {parsed_fmt}")
    db = SQLamarr.SQLite3DB(parsed_fmt)
    db.seed(tid)
    loader = self.loader(db)

    clean = SQLamarr.Pipeline([SQLamarr.CleanEventStore(db)])

    pipeline = SQLamarr.Pipeline([
      make_algo(db) for _, make_algo in self.sequence
      ])

    self.logger.info(f"Algorithms: {', '.join(name for name, _ in self.sequence)}")

    for batch in self._batched (load_args, self.batch):
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









    


