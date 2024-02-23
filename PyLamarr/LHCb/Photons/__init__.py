from .PyPhotons import PyPhotons
#------------------------------#

def configure_pipeline():
  return [
      ("MkPhotons", PyPhotons),
      ]

