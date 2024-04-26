import numpy as np 
import logging
from typing import Collection, Union, Dict, Optional, Any
from dataclasses import dataclass

import PyLamarr

@dataclass
class UprootEventBatch (PyLamarr.EventBatch):
    dataframe_dict: Dict[str, Any] = None
    database: Any = None
    bid_var: Collection[str] = None
    batch_selector: Any = None

    def load(self):
        with self.database.connect() as c:
            for name, df in self.dataframe_dict.items():
                (
                        df[df[self.bid_var] == self.batch_selector]
                        .drop(columns=[self.bid_var])
                        .to_sql(name, c, if_exists='append', index=False)
                )

class UprootLoader:
    """
    Ease loading nTuples generated with Gaussino into the SQLite 
    event model of Lamarr.
    As the other python data loaders, UprootLoader should be configured in the 
    constructor.
    The configured object is then called during the event loop to 
    pass the updated connection to the SQLamarr.SQLite3DB instance.

    The ROOT file with path `input_file` is expected contain a 
    `TDirectory` (named as configured 
    with the `collector` keyword) with a `TTree` per SQLite table (the 
    names of the `TTree`s are listed in `tables`) and each `TTree` should 
    include a column (titled as indicated by `batch_id_var`) providing 
    a unique identifier for the event number.

    """
    def __init__ (self, 
            input_file: str, 
            tables: Collection[str], 
            collector: str = 'LamarrCollector', 
            batch_id_var: str = 'batch_id',
            max_rows: Union[int, None] = None
            ):

        import uproot 
        import pandas as pd 

        self.input_file = input_file
        self.tables = tables
        self.bid_var = batch_id_var
        self._db = None
        root_dir = uproot.open(input_file)[collector]

        self._batch_codes = np.unique(
                root_dir[tables[0]].arrays(self.bid_var, library='np', entry_stop=max_rows)[self.bid_var]
                )

        self._dataframe = {
                n: pd.DataFrame(root_dir[n].arrays(library='np', entry_stop=max_rows)) for n in self.tables
                } 

        self.logger = logging.getLogger(self.__class__.__name__)

    @property 
    def batches(self):
        return np.arange(len(self._batch_codes))


    def __call__(self, db):
        self._db = db
        return self


    def load(self, batch):
        if self._db is None:
            raise ValueError("PandasLoader tried loading with uninitialized db.\n"
                    "Missed ()?")
        
        self.logger.debug(f"Preparing uproot loader for batch {batch}")
        yield UprootEventBatch(
            description=f"batch_id: {batch}",
            dataframe_dict=self._dataframe,
            database=self._db,
            bid_var=self.bid_var,
            batch_selector=self._batch_codes[batch],
        )
