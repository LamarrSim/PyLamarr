"""
TTreeLoader.
"""
import sys
import pandas as pd 
import numpy as np 

class TTreeLoader:
    def __init__(self, database_connection):
        self._db = database_connection

    def load(self, filename, batch_id=0, tables=None, if_exists='replace'):
        ## Load optional dependency uproot
        try:
            import uproot
        except ImportError as e:
            print ("The uproot package is required for loading ROOT files "
                   "with TTreeLoader. \nInstall it with `pip install uproot`",
                   file=sys.stderr)
            raise e

        ## Ensure tables is iterable
        if isinstance(tables, str):
            tables = [tables] 

        ## Open the file
        input_file = uproot.open(filename)

        ## Connect to the database
        with self._db.connect() as db:
            # Loop on the objects in the ROOT file
            for key in input_file.keys():
                ## Object Lookup 
                obj = input_file[key]

                ## Filter on object type (requires TTree)
                if not isinstance(obj, uproot.behaviors.TTree.TTree):
                    continue 

                ## Filter on selected tables (requires key in table)
                if tables is not None and all([key not in t for t in tables]):
                    continue

                df = pd.DataFrame(
                    obj.arrays(library='np')
                    )
                df['input_file'] = batch_id
                df.to_sql(obj.name, db, if_exists=if_exists)

                












