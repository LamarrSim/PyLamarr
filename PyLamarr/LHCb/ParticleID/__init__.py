from functools import partial

from .GanPipeline import GanPipeline
from .IsMuonEfficiency import IsMuonEfficiency 
from .AssignIsMuon import AssignIsMuon

## Helper
from .configure_pipeline import configure_pipeline as configure_pipeline_generic

configure_pipeline = partial(configure_pipeline_generic,
    library="https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
            "models/lhcb.pid.2016MU-sim.so") 
