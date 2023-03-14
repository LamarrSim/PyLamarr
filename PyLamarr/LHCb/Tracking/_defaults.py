from pydantic import Field
from PyLamarr import RemoteResource


default_lib = ("https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
               "models/lhcb.trk.2016MU.20230128.so")
    
default_lib_field = Field(default_factory=lambda: RemoteResource(default_lib))

