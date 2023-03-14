from typing import Tuple, Optional, Union
from dataclasses import dataclass

from pydantic import validate_arguments, validator

from PyLamarr import RemoteResource
import SQLamarr

@validate_arguments
@dataclass(frozen=True)
class AssignIsMuon:
  ismuoneff_table: str
  output_table: str = "tmp_is_muon"
  output_columns: Tuple[str, ...] = ("mcparticle_id", "ismuoneff", "is_muon")
  make_persistent: bool = True

  def query(self):
    return f"""
    SELECT 
      mcparticle_id AS mcparticle_id,
      isMuonEff,
      random_category(1-isMuonEff, isMuonEff) AS isMuon
    FROM {self.ismuoneff_table};
    """

  def __call__(self, db):
    return SQLamarr.TemporaryTable(db,
        self.output_table,
        self.output_columns,
        self.query(),
        self.make_persistent
        )

