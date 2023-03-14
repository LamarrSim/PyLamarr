from typing import Tuple, Optional, Union
from dataclasses import dataclass

from pydantic import validate_arguments, validator

from PyLamarr import RemoteResource
import SQLamarr

@validate_arguments
@dataclass(frozen=True)
class IsMuonEfficiency:
  library: RemoteResource
  symbol: str
  output_table: str
  abs_mcid: int
  particle_table: Optional[str] = "MCParticles"
  track_table: Optional[str] = "tmp_particles_recoed_as"
  track_type: Optional[int] = 3
  references: Optional[Tuple[str, ...]] = ( "mcparticle_id", )
  output_columns: Optional[Tuple[str, ...]] = ( "IsMuonEff", )


  def query(self):
    return f"""
    SELECT 
      p.mcparticle_id AS mcparticle_id,
      norm2(p.px, p.py, p.pz) AS p,
      pseudorapidity(p.px, p.py, p.pz) AS eta,
      random_normal() * 10 + 100 as nTracks,
      propagation_charge(p.pid) AS track_charge,
      0 AS isMuon
    FROM {self.particle_table} AS p
    INNER JOIN {self.track_table} AS recguess 
      ON p.mcparticle_id = recguess.mcparticle_id
    WHERE 
        recguess.track_type == {self.track_type}
      AND 
        abs(p.pid) == {self.abs_mcid};
    """


  def __call__(self, db):
    return SQLamarr.Plugin(db,
        self.library.file,
        self.symbol,
        self.query(),
        self.output_table,
        self.output_columns,
        self.references,
        )




