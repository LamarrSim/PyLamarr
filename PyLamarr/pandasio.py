import pandas as pd

from dataclasses import dataclass, field
from typing import List, Optional
from SQLamarr import SQLite3DB
import PyLamarr


class PandasDataLoader:
    def __init__(self, db: SQLite3DB):
        self._connection = db

    def load(self, accept_multiple_batches: bool = False, **dataframes):
        with self._connection.connect() as db:
            for table, df in dataframes.items():
                df.to_sql(table, db, if_exists='append', index=False)
                res = db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
                table_len = res[0] if len(res) else 0
                if table_len != len(df) and accept_multiple_batches is False:
                    raise AttributeError("Handling multiple")


@dataclass
class OutputCollector:
    table: str
    dataframes: List[pd.DataFrame] = field(default_factory=lambda: [])
    batch_ids: Optional[List[int]] = None

    @PyLamarr.method
    def __call__(self, db):
        self.dataframes.append(pd.read_sql_query(f"SELECT * FROM {self.table}", db))

    @property
    def dataframe(self):
        batch_ids = self.batch_ids if self.batch_ids is not None else list(range(len(self.dataframes)))
        dataframes = [df.assign(batch_id=bid) for bid, df in zip(batch_ids, self.dataframes)]
        return pd.concat(dataframes, ignore_index=True)

