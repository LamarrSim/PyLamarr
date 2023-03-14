## Default logger configuration
import logging 

def configure_logger(format=None, level=None, datefmt=None):
  logging.basicConfig(
      format=format or "%(asctime)s | %(name)-20s | %(levelname)-7s | %(message)s", 
      level=level or logging.WARNING, 
      datefmt=datefmt or '%Y-%m-%d %H:%M:%S %Z'
      )


from PyLamarr.RemoteResource import RemoteResource
from PyLamarr.function import function
from PyLamarr.Concatenate import Concatenate

