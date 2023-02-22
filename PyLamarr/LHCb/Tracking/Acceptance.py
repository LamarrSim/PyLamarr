from typing import Tuple
from PyLamarr import RemoteResource
import SQLamarr

class Acceptance:
  def __init__ (self,
      url: str = "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
                 "models/lhcb.trk.2016MU.20230128.so",
      symbol: str = "acceptance",
      output_table: str = "tmp_acceptance_out",
      output_columns: Tuple[str] = ("acceptance",),
      references: Tuple[str] = ("mcparticle_id", )
      ):

    self._library = RemoteResource(url)
    self._symbol = symbol
    self._output_table = output_table
    self._output_columns = output_columns
    self._references = references

  def query(self):
    return """
        SELECT 
          mcparticle_id,
          ov.x AS mc_x, 
          ov.y AS mc_y, 
          ov.z AS mc_z,
          log10(norm2(p.px, p.py, p.pz)) AS mc_log10_p,
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

  def __call__(self, db):
    return SQLamarr.Plugin(db,
        self._library.file,
        self._symbol,
        self.query(),
        self._output_table,
        self._output_columns,
        self._references,
        )

