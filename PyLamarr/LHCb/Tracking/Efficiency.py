from typing import Tuple, Optional
from dataclasses import dataclass
from PyLamarr import RemoteResource, Wrapper

from pydantic import validate_arguments

from ._defaults import default_lib_field


@validate_arguments
@dataclass(frozen=True)
class Efficiency(Wrapper):
    library: RemoteResource = default_lib_field
    symbol: str = "efficiency"
    output_table: str = "tmp_efficiency_out"
    output_columns: Tuple[str, ...] = (
        "not_recoed", "long", "upstream", "downstream"
    )
    references: Tuple[str, ...] = ("mcparticle_id",)

    def query(self):
        return """
        SELECT 
          mcparticle_id,
          ov.x AS mc_x, 
          ov.y AS mc_y, 
          ov.z AS mc_z,
          log(norm2(p.px, p.py, p.pz))/log(10.) AS mc_log10_p,
          p.px/p.pz AS mc_tx, 
          p.py/p.pz AS mc_ty,
          pseudorapidity(p.px, p.py, p.pz) AS mc_eta,
          azimuthal(p.px, p.py, p.pz) AS mc_phi,
          abs(p.pid) == 11 AS mc_is_e,
          abs(p.pid) == 13 AS mc_is_mu,
          (
            abs(p.pid) == 211 OR abs(p.pid) == 321 OR abs(p.pid) == 2212  
          ) AS mc_is_h,
          propagation_charge(p.pid) AS mc_charge
        FROM MCParticles AS p
        INNER JOIN MCVertices AS ov ON p.production_vertex = ov.mcvertex_id
        WHERE 
          p.pz > 1.
          AND
          propagation_charge(p.pid) <> 0.
          """

    implements: str = "Plugin"

    @property
    def config(self):
        return dict(
            library_path=self.library,
            function_name=self.symbol,
            query=self.query(),
            output_table=self.output_table,
            outputs=self.output_columns,
            references=self.references,
        )
