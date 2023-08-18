from . import ( Acceptance, 
                Efficiency, 
                AssignCategory, 
                PropagateToClosestToBeam, 
                Resolution, 
                Covariance
                )

def configure_pipeline(library: str):
    return (
        ('TrkAcc',         Acceptance(library=library)),
        ('TrkEff',         Efficiency(library=library)),
        ('TrkAssign',      AssignCategory()),
        ('Propagate2CTB',  PropagateToClosestToBeam()),
        ('TrkResolution',  Resolution(library=library)),
        ('TrkCovariance',  Covariance(library=library)),
        )
