from PyLamarr import RemoteResource 
from . import ( Acceptance, 
                Efficiency, 
                AssignCategory, 
                PropagateToClosestToBeam, 
                Resolution, 
                Covariance,
                CovariancePostprocessing,
                ParticleMaker
                )
from ._defaults import default_lib

def configure_pipeline(*_, library: RemoteResource = default_lib):
    if isinstance(library, str):
        library = RemoteResource(library)

    return (
        ('TrkAcc',         Acceptance(library=library)),
        ('TrkEff',         Efficiency(library=library)),
        ('TrkAssign',      AssignCategory()),
        ('Propagate2CTB',  PropagateToClosestToBeam()),
        ('TrkResolution',  Resolution(library=library)),
        ('TrkCovariance',  Covariance(library=library)),
        ('TrkCovPostPro',  CovariancePostprocessing()),
        ('Maker',          ParticleMaker()),
        )
