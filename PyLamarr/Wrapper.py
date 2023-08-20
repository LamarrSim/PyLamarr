import xml.etree.ElementTree as e3
from functools import wraps
import logging

from dataclasses import dataclass, field, KW_ONLY, fields
from typing import Dict, Any, List, Optional, Tuple, Union
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
        except (TypeError, AttributeError) as e:
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



## Decorator
class persistent_table:
    def __init__(self, 
        output_columns: List[str], 
        make_persistent: Optional[bool] = True
        ):
        self.output_columns = output_columns
        self.make_persistent = make_persistent

    def __call__(self, query_func):
        @wraps(query_func)
        @validate_arguments
        @dataclass(frozen=True)
        class _Wrapped(Wrapper):
            output_table: Optional[str] = query_func.__name__
            output_columns: Optional[Tuple[str, ...]] = self.output_columns
            make_persistent: Optional[bool] = self.make_persistent

            def query(s):
                return query_func()

            implements: str = "TemporaryTable"

            @property
            def config(s):
                return dict(
                    output_table=s.output_table,
                    outputs=s.output_columns,
                    query=s.query(),
                    make_persistent=s.make_persistent,
                )

        return _Wrapped



## Function
@validate_arguments
def custom_query(query: Union[str,List[str]]):
    @validate_arguments
    @dataclass(frozen=True)
    class _Wrapped(Wrapper):
        replacements: Optional[Dict[str,str]] = field(default_factory=dict)
        implements: str = "EditEventStore"

        @property
        def config(s):
            return dict(
                queries=(query.format(**s.replacements) if isinstance(query,str) 
                         else [q.format(**s.replacements) for q in query])
                )

    return _Wrapped

