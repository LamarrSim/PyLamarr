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
            z_closest_to_beam(gv.x, gv.y, gv.z, p.px/p.pz, p.py/p.pz) AS z,
            gv.x AS x0,
            gv.y AS y0,
            gv.z AS z0,
            p.px/p.pz AS tx,
            p.py/p.pz AS ty
          FROM MCParticles AS p
          JOIN GenParticles AS gp ON gp.genparticle_id == p.genparticle_id
          JOIN GenVertices as gv ON gp.production_vertex == gv.genvertex_id
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
