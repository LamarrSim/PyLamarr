from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments

from PyLamarr import RemoteResource, Wrapper


@validate_arguments
@dataclass(frozen=True)
class ParticleMaker(Wrapper):
    output_table: Optional[str] = "particles"
    output_columns: Optional[Tuple[str, ...]] = (
        "mcparticle_id", "track_type",
        "dx", "dy", "dz", "dtx", "dty", "dp",
        "chi2PerDoF", "nDoF_f", "ghostProb"
      )
    make_persistent: Optional[bool] = True

    def query(self):
        return """
          SELECT 
            reco.mcparticle_id AS mcparticle_id,
            reco.track_type AS track_type,
            res.dx, res.dy, res.dz, res.dtx, res.dty, res.dp,
            res.chi2PerDoF, res.nDoF_f, res.ghostProb
          FROM tmp_particles_recoed_as AS reco
          LEFT JOIN tmp_resolution_out AS res ON reco.mcparticle_id == res.mcparticle_id
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

