import PyLamarr

from dataclasses import dataclass, field
from typing import Collection, List, Optional, Dict, Union
import pandas as pd 
import logging

@dataclass
class PandasCollector:
    tables: Collection[str]
    dataframes: Dict[str,List[Union[pd.DataFrame, None]]] = field(default_factory=lambda: {})
    batch_ids: Optional[List[int]] = None

    @PyLamarr.method
    def __call__(self, db):
      logger = logging.getLogger("PandasCollector")
      existing_tables = pd.read_sql_query(f"SELECT name FROM sqlite_master WHERE type == 'table'", db)['name'].values.tolist()
      for table in self.tables:
          if table not in self.dataframes.keys():
            self.dataframes[table] = list()

          if table in existing_tables:
            df = pd.read_sql_query(f"SELECT * FROM {table}", db)
            self.dataframes[table].append(df)
            logger.debug(f"Table {table}, requested for collection, contains {len(df)} rows.")
          else:
            self.dataframes[table].append(None)
            logger.debug(f"Table {table}, requested for collection, NOT FOUND.")

    @property
    def dataframe(self):
        ret = {}

        for table, dfs in self.dataframes.items():
            batch_ids = self.batch_ids if self.batch_ids is not None else list(range(len(dfs)))
            dataframes = [df.assign(batch_id=bid) for bid, df in zip(batch_ids, dfs) if df is not None and len(df) > 0]
            # If there is at least one dataframe with entries, it includes the entry and moves forward
            if len(dataframes):
              ret[table] = pd.concat(dataframes, ignore_index=True)
            # If dataframes are all empty, it picks the first one to avoid errors downstream for missing table
            elif any([len(df) > 0 for df in dfs]):
              ret[table] = [df for df in dfs if len(df) > 0][0]
              ret[table]['batch_id'] = []

        return ret




