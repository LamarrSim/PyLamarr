import PyLamarr

from dataclasses import dataclass, field
from typing import List, Optional, Dict
import pandas as pd 

@dataclass
class PandasCollector:
    tables: List[str]
    dataframes: Dict[str,List[pd.DataFrame]] = field(default_factory=lambda: {})
    batch_ids: Optional[List[int]] = None

    @PyLamarr.method
    def __call__(self, db):
      existing_tables = pd.read_sql_query(f"SELECT name FROM sqlite_master WHERE type == 'table'", db)['name'].values.tolist()
      for table in self.tables:
          if table not in self.dataframes.keys():
            self.dataframes[table] = list()

          if table in existing_tables:
            self.dataframes[table].append(pd.read_sql_query(f"SELECT * FROM {table}", db))
          else:
            self.dataframes[table].append(None)

    @property
    def dataframe(self):
        ret = {}

        for table, dfs in self.dataframes.items():
            batch_ids = self.batch_ids if self.batch_ids is not None else list(range(len(dfs)))
            dataframes = [df.assign(batch_id=bid) for bid, df in zip(batch_ids, dfs) if df is not None]
            if len(dataframes):
              ret[table] = pd.concat(dataframes, ignore_index=True)

        return ret




