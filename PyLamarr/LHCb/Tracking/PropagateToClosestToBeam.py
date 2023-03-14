from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments

from PyLamarr import RemoteResource
import SQLamarr

@validate_arguments
@dataclass(frozen=True)
class PropagateToClosestToBeam:
  output_table: Optional[str] = "tmp_closest_to_beam"
  output_columns: Optional[Tuple[str, ...]] = ("mcparticle_id", "x", "y", "z")
  make_persistent: Optional[bool] = True

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
        self.output_table,
        self.output_columns,
        self.query(),
        self.make_persistent,
        )



