from typing import Tuple
from PyLamarr import RemoteResource
import SQLamarr

class PropagateToClosestToBeam:
  def __init__ (self,
      output_table: str = "tmp_closest_to_beam",
      output_columns: Tuple[str] = ("mcparticle_id", "x", "y", "z"),
      make_persistent: bool = True,
      ):

    self._output_table = output_table
    self._output_columns = output_columns
    self._make_persistent = make_persistent

  def query(self):
    return """
        WITH ctb AS (
          SELECT 
            mcparticle_id,
            z_closest_to_beam(ov.x, ov.y, ov.z, p.px/p.pz, p.py/p.pz) AS z,
            ov.x AS x0,
            ov.y AS y0,
            ov.z AS z0,
            p.px/p.pz AS tx,
            p.py/p.pz AS ty
          FROM MCParticles AS p
          INNER JOIN MCVertices AS ov
            ON p.production_vertex = ov.mcvertex_id
        )
        SELECT 
          mcparticle_id,
          x0 + (z - z0)*tx AS x,
          y0 + (z - z0)*ty AS y,
          z AS z
        FROM ctb;
      """

  def __call__(self, db):
    return SQLamarr.TemporaryTable(db,
        self._output_table,
        self._output_columns,
        self.query(),
        self._make_persistent,
        )



