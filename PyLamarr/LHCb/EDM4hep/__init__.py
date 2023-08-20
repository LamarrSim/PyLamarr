from .adapters import (
    EventHeader,
    MCParticle,
    MCParticle__parents__MCParticle,
    MCParticle__daughters__MCParticle,
    ParticleID,
    Track,
    LHCbTrackState,
    Vertex,
    ReconstructedParticle,
    CleanUp,
    )

def configure_pipeline():
  return [
      ('EDM4hep::EventHeader', EventHeader()),
      ('EDM4hep::MCParticle', MCParticle()),
      ('EDM4hep::MCParticle_parent', MCParticle__parents__MCParticle()),
      ('EDM4hep::MCParticle_daughter', MCParticle__daughters__MCParticle()),
      ('EDM4hep::ParticleID', ParticleID()),
      ('EDM4hep::Track', Track()),
      ('EDM4hep::TrackState', LHCbTrackState()),
      ('EDM4hep::Vertex', Vertex()),
      ('EDM4hep::RecoParts', ReconstructedParticle()),
      ('CleanUp::MCParticles', CleanUp()),
      ]

