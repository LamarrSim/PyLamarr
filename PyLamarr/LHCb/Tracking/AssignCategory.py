from typing import Tuple
from PyLamarr import RemoteResource
import SQLamarr

class AssignCategory:
  def __init__ (self,
      output_table: str = "tmp_particles_recoed_as",
      output_columns: Tuple[str] = ("mcparticle_id", "track_type"),
      make_persistent: bool = True,
      ):

    self._output_table = output_table
    self._output_columns = output_columns
    self._make_persistent = make_persistent

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
        self._output_table,
        self._output_columns,
        self.query(),
        self._make_persistent,
        )


