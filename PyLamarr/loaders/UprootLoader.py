import numpy as np 
from typing import List

from PyLamarr.loaders import PandasLoader

class UprootLoader:
    """
    Ease loading nTuples generated with Gaussino into the SQLite 
    event model of Lamarr.
    As the other python data loaders, PandasLoader should be configured in the 
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
            tables: List[str], 
            collector: str = 'LamarrCollector', 
            batch_id_var: str = 'batch_id'
            ):

        import uproot 
        import pandas as pd 

        self.input_file = input_file
        self.tables = tables
        self.bid_var = batch_id_var
        self._db = None
        root_dir = uproot.open(input_file)[collector]

        self._batches = np.unique(
                root_dir[tables[0]].arrays(self.bid_var, library='np')[self.bid_var]
                )

        self._dataframe = {
                n: pd.DataFrame(root_dir[n].arrays(library='np')) for n in self.tables
                } 


    @property 
    def batches(self):
        return np.arange(len(self._batches))


    def __call__(self, db):
        self._db = db
        return self


    def load(self, batch):
        if self._db is None:
            raise ValueError("PandasLoader tried loading with uninitialized db.\n"
                    "Missed ()?")

        with self._db.connect() as c:
            for name, df in self._dataframe.items():
                (
                        df[df[self.bid_var] == self.batches[batch]]
                        .drop(columns=[self.bid_var])
                        .to_sql(name, c, if_exists='append', index=False)
                )
