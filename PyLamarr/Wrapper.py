import xml.etree.ElementTree as e3
import logging

from dataclasses import dataclass, field, KW_ONLY, fields
from typing import Dict, Any
from pydantic import validate_arguments
import ctypes

from PyLamarr.RemoteResource import RemoteResource


@dataclass(frozen=True)
class Wrapper:
    def __call__(self, db):
        import SQLamarr
        try:
            config = {k: v.file if isinstance(v, RemoteResource) else v 
                      for k, v in self.get_config().items()}

            return getattr(SQLamarr, self.get_imp())(db, **config)
        except (TypeError, ctypes.AttributeError) as e:
            logging.getLogger("Wrapper").error(
                f"Error while configuring {self.__class__.__name__} "
                f"as {self.get_imp()}"
            )
            raise e

    def get_imp(self):
        if hasattr(self, "implements"):
            return getattr(self, "implements")
        raise AttributeError("Class derived from Wrapper does not implement `implements` property")

    def get_config(self):
        if not hasattr(self, "config"):
          raise AttributeError("Class derived from Wrapper does not implement `config` property")

        if 'query' in self.config.keys() and len(self.config['query']) > 16384:
          raise ValueError("Length of the query [{self.__class__.__name__}] exceeds maximum length of 16384 bytes") 

        return getattr(self, "config")



    def to_xml(self, parent_node):
        node = e3.SubElement(
            parent_node,
            self.implements,
            name=self.__class__.__name__
        )

        for k, v in self.config.items():
            print ("#=#=#=#=")
            print (k, v, type(v))
            if isinstance(v, RemoteResource):
                e3.SubElement(node, "CONFIG", key=k, type='url').text = v.remote_url
            elif isinstance(v, (list, tuple, set)):
                e3.SubElement(node, "CONFIG", key=k, type='seq').text = ";".join(v)
            else:
                e3.SubElement(node, "CONFIG", key=k, type='str').text = str(v)

        return node


@validate_arguments
@dataclass(frozen=True)
class GenericWrapper(Wrapper):
    implements: str
    config: Dict[str, Any] = field(default_factory=dict)
