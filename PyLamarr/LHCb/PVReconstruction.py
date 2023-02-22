from typing import Union
import SQLamarr
from PyLamarr import RemoteResource


def PVReconstruction(
    condition: str,
    url: Union[str, None] = None,
    table: str = "PVSmearing"
    ):
  _pvdb = RemoteResource(url if url is not None else
      "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
      "PrimaryVertex/PrimaryVertexSmearing.db"
      )

  return lambda db: SQLamarr.PVReconstruction(db, _pvdb.file, table, condition)

