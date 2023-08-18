from functools import partial

from .Acceptance import Acceptance
from .Efficiency import Efficiency
from .AssignCategory import AssignCategory
from .PropagateToClosestToBeam import PropagateToClosestToBeam
from .Resolution import Resolution
from .Covariance import Covariance
from .CovariancePostprocessing import CovariancePostprocessing

from ._defaults import default_lib
from .configure_pipeline import configure_pipeline as configure_pipeline_generic
configure_pipeline = partial(configure_pipeline_generic, default_lib)


