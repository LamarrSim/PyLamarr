from typing import Tuple, Optional, Union
from dataclasses import dataclass

from pydantic import validate_arguments, validator

from PyLamarr import RemoteResource
import SQLamarr

@validate_arguments
@dataclass(frozen=True)
class Concatenate:
  output_table: str
  input_tables: Tuple[str, ...]
  columns: Tuple[str, ...]
  make_persistent: bool = True

  def query(self):
    return list(
        f"SELECT {', '.join(self.columns)} FROM {t}" for t in self.input_tables
        )

  def __call__(self, db):
    return SQLamarr.TemporaryTable(db,
        output_table=self.output_table,
        outputs=self.columns,
        query=self.query(),
        make_persistent=self.make_persistent
        )





