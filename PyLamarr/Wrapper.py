import xml.etree.ElementTree as e3
import logging 

from dataclasses import dataclass, field, KW_ONLY, fields
from typing import Dict, Any
from pydantic import validate_arguments
import ctypes

@dataclass(frozen=True)
class Wrapper:
  def __call__(self, db):
    import SQLamarr
    try:
      return getattr(SQLamarr, self.implements)(db, **self.config)
    except (TypeError, ctypes.AttributeError) as e:
      logging.getLogger("Wrapper").error(
          f"Error while configuring {self.__class__.__name__} "
          f"as {self.implements}"
          )
      raise e

  def to_xml(self, parent_node):
    node = e3.SubElement(
        parent_node, 
        self.implements, 
        name=self.__class__.__name__
        )

    for k, v in self.config.items():
      if isinstance(v, (list,tuple,set)):
        e3.SubElement(node, "CONFIG", key=k, type='seq').text = ";".join(v)
      else:
        e3.SubElement(node, "CONFIG", key=k, type='str').text = str(v)

    return node



@validate_arguments
@dataclass(frozen=True)
class GenericWrapper(Wrapper):
  implements: str
  config: Dict[str, Any] = field(default_factory=dict)


