from typing import Union, Optional
from pydantic import validate_arguments, Field
from dataclasses import dataclass, InitVar
from PyLamarr import RemoteResource as RemoteRes
from PyLamarr import Wrapper

PV_LIB = ("https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
          "PrimaryVertex/PrimaryVertexSmearing.db")


@validate_arguments
@dataclass(frozen=True)
class PVReconstruction(Wrapper):
    """
  Parametrize the reconstruction of a Primary Vertex.


  @param condition: Data-taking condition, e.g. `2016_pp_MagUp`;
  @param library: RemoteResource (or simply an URL) to the SQLite DB with 
      parametrizations;
  @param table: name of the SQLite table to read the parametrization from

  ```python
  db = SQLamarr.SQLite3DB(parsed_fmt)
  pv_reco = PVReconstruction('2016_pp_MagUp')
  pv_reco (db)
  ```

  @see SQLamarr.PVReconstruction: C++ implementation of the algorithm

  """

    condition: str
    library: Optional[RemoteRes] = Field(default_factory=lambda: RemoteRes(PV_LIB))
    table: Optional[str] = "PVSmearing"

    implements: str = "PVReconstruction"

    @property
    def config(self):
        """@private Call method"""
        return dict(
            file_name=self.library.file,
            table_name=self.table,
            condition=self.condition
        )
