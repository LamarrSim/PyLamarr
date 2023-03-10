from typing import Tuple
from PyLamarr import RemoteResource
import SQLamarr

class Covariance:
  def __init__ (self,
      url: str = "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
                 "models/lhcb.trk.2016MU.20230128.so",
      symbol: str = "covariance",
      output_table: str = "tmp_covariance_out",
      output_columns: Tuple[str] = (
          "log_cov_ClosestToBeam_0_0",
          "log_cov_ClosestToBeam_1_1",
          "log_cov_ClosestToBeam_2_2",
          "log_cov_ClosestToBeam_3_3",
          "log_cov_ClosestToBeam_4_4",
          "corr_ClosestToBeam_0_1",
          "corr_ClosestToBeam_0_2",
          "corr_ClosestToBeam_1_2",
          "corr_ClosestToBeam_0_3",
          "corr_ClosestToBeam_1_3",
          "corr_ClosestToBeam_2_3",
          "corr_ClosestToBeam_0_4",
          "corr_ClosestToBeam_1_4",
          "corr_ClosestToBeam_2_4",
          "corr_ClosestToBeam_3_4"
        ),
      n_random: int = 128,
      references: Tuple[str] = ("mcparticle_id", )
      ):

    self._library = RemoteResource(url)
    self._symbol = symbol
    self._output_table = output_table
    self._output_columns = output_columns
    self._n_random = n_random
    self._references = references

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
          tmpres.chi2PerDoF AS chi2PerDoF,
          tmpres.nDoF_f AS nDoF_f,
          tmpres.ghostProb AS ghostProb,
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
        INNER JOIN tmp_resolution_out AS tmpres 
          ON p.mcparticle_id = tmpres.mcparticle_id
        INNER JOIN tmp_closest_to_beam AS ctb 
          ON p.mcparticle_id = ctb.mcparticle_id
        WHERE 
          recguess.track_type IN (3, 4, 5)
          """

  def __call__(self, db):
    return SQLamarr.GenerativePlugin(db,
        self._library.file,
        self._symbol,
        self.query(),
        self._output_table,
        self._output_columns,
        self._n_random,
        self._references,
        )

