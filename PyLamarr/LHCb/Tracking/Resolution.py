from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments
from PyLamarr import RemoteResource
import SQLamarr

from ._defaults import default_lib_field

@validate_arguments
@dataclass(frozen=True)
class Resolution:
  library: Optional[str] = default_lib_field
  symbol: Optional[str] = "resolution"
  output_table: Optional[str] = "tmp_resolution_out"
  output_columns: Optional[Tuple[str, ...]] = (
    "dx", "dy", "dz", "dtx", "dty", "dp",
    "chi2PerDoF", "nDoF_f", "ghostProb"
    )
  n_random: int = 128
  references: Optional[Tuple[str, ...]] = ("mcparticle_id", )


  def query(self):
    return """
        SELECT 
          p.mcparticle_id,
          ctb.x AS mc_x, 
          ctb.y AS mc_y, 
          ctb.z AS mc_z, 
          p.px/p.pz AS mc_tx, 
          p.py/p.pz AS mc_ty,
          log10(norm2(p.px, p.py, p.pz)) AS mc_log10_p,
          abs(p.pid) == 11 AS mc_is_e,
          abs(p.pid) == 13 AS mc_is_mu,
          (abs(p.pid) = 211 OR abs(p.pid) = 321 OR abs(p.pid) = 2212) AS is_h,
          (recguess.track_type == 3) AS is_long, 
          (recguess.track_type == 4) AS is_upstream, 
          (recguess.track_type == 5) AS is_downstream 
        FROM MCParticles AS p
        INNER JOIN MCVertices AS ov ON p.production_vertex = ov.mcvertex_id
        INNER JOIN tmp_particles_recoed_as AS recguess 
          ON p.mcparticle_id = recguess.mcparticle_id
        INNER JOIN tmp_closest_to_beam AS ctb 
          ON p.mcparticle_id = ctb.mcparticle_id
        WHERE 
          recguess.track_type IN (3, 4, 5);
          """

  def __call__(self, db):
    return SQLamarr.GenerativePlugin(db,
        self.library.file,
        self.symbol,
        self.query(),
        self.output_table,
        self.output_columns,
        self.n_random,
        self.references,
        )

