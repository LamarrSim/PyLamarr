import PyLamarr
from functools import partial

class PandasLoader:
    """
    Ease loading a set of pandas DataFrames to the SQLite event model.
    As the other python data loaders, PandasLoader should be configured in the 
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

        with self._db.connect() as c:
            for name, df in dataframe_dict.items():
                df.to_sql(name, c, **self._kwargs)


        

