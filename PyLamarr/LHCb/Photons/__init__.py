from typing import Union

from .PyPhotons import PyPhotons
#------------------------------#

def configure_pipeline(efficiency_model: Union[str, None], resolution_model: Union[str, None]):
  return [
      ("MkPhotons", PyPhotons(efficiency_model=efficiency_model, resolution_model=resolution_model)),
      ]

