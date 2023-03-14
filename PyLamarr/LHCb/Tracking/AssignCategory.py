from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments

from PyLamarr import RemoteResource
import SQLamarr


@validate_arguments
@dataclass(frozen=True)
class AssignCategory:
  output_table: Optional[str] = "tmp_particles_recoed_as"
  output_columns: Optional[Tuple[str, ...]] = ("mcparticle_id", "track_type")
  make_persistent: Optional[bool] = True

  def query(self):
    return """
      SELECT 
        eff.mcparticle_id,
        random_category(not_recoed, 0, 0, long, upstream) AS track_type
      FROM tmp_efficiency_out AS eff
      INNER JOIN tmp_acceptance_out AS acc
        ON eff.mcparticle_id = acc.mcparticle_id
      WHERE random_category(1 - acc.acceptance, acc.acceptance) == 1;
      """

  def __call__(self, db):
    return SQLamarr.TemporaryTable(db,
        self.output_table,
        self.output_columns,
        self.query(),
        self.make_persistent,
        )


