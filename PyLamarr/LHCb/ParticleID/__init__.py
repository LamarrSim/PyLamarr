from functools import partial

from .GanPipeline import GanPipeline
from .IsMuonEfficiency import IsMuonEfficiency
from .AssignIsMuon import AssignIsMuon

# Helper
from .configure_pipeline import configure_pipeline as configure_pipeline_generic

configure_pipeline = partial(
    configure_pipeline_generic,
    library="https://gitlab.cern.ch/lhcb-datapkg/LamarrData/-/raw/v3r0/data/"
            "ChargedPID/2016/compiledmodel_2016-MagUp-sim.so?inline=false"
)
