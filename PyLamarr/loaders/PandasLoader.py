import PyLamarr
from functools import partial
from dataclasses import dataclass
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class PandasEventBatch (PyLamarr.EventBatch):
    dataframe_dict: Dict[str, Any] = None
    database: Any = None

    def load(self):
        with self.database.connect() as c:
            for name, df in self.dataframe_dict.items():
                df.to_sql(name, c, **self._kwargs)



class PandasLoader:
    """
    Ease loading a set of pandas DataFrames to the SQLite event model.
    As the other python test_data loaders, PandasLoader should be configured in the
    constructor.
    The configured object is then called during the event loop to 
    pass the updated connection to the SQLamarr.SQLite3DB instance.

    The configuration keyword-arguments passed to the constructor are passed 
    to the pandas.DataFrame.to_sql function. 

    Some default values, however, is overridden as much more commonly adopted 
    in the context of Lamarr. In particular,
     * `if_exists` defaults to `"append"`
     * `index` defaults to `False`


    """
    def __init__(self, 
            **to_sql_kwargs
            ):
        self._db = None

        ## Override of the default values
        self._kwargs = dict(if_exists='append', index=False)
        self._kwargs.update(to_sql_kwargs)

    def __call__(self, database):
        self._db = database
        return self

    def load(self, **dataframe_dict):
        """
        Internal. 
        """
        if self._db is None:
            raise ValueError("PandasLoader tried loading with uninitialized db.\n"
                    "Missed ()?")

        yield PandasEventBatch(dataframe_dict=dataframe_dict, database=self._db)


        

