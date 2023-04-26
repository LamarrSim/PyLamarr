from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments

from PyLamarr import Wrapper


@validate_arguments
@dataclass(frozen=True)
class PropagateToClosestToBeam(Wrapper):
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

    implements: str = "TemporaryTable"

    @property
    def config(self):
        return dict(
            output_table=self.output_table,
            outputs=self.output_columns,
            query=self.query(),
            make_persistent=self.make_persistent,
        )
