from typing import Tuple, Optional, Union
from dataclasses import dataclass

from pydantic import validate_arguments, validator

from PyLamarr import RemoteResource, Wrapper

@validate_arguments
@dataclass(frozen=True)
class AssignIsMuon(Wrapper):
  ismuoneff_table: str
  output_table: str = "tmp_is_muon"
  output_columns: Tuple[str, ...] = ("mcparticle_id", "ismuoneff", "is_muon")
  make_persistent: bool = True

  def query(self):
    return f"""
    SELECT 
      mcparticle_id AS mcparticle_id,
      isMuonEff,
      random_category(1-isMuonEff) AS isMuon
    FROM {self.ismuoneff_table};
    """


  implements: str = "TemporaryTable"
  @property
  def config(self):
    return dict(
        output_table=self.output_table,
        outputs=self.output_columns,
        query=self.query(),
        make_persistent=self.make_persistent
        )

