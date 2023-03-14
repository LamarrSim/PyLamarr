import os
import logging
import hashlib

from pydantic import BaseModel, PrivateAttr, validator
from typing import Optional

import requests

class RemoteResource (BaseModel):
  remote_url: str
  local_filename: Optional[str] = None
  _file: Optional[str] = PrivateAttr()

  def __init__ (self, *args, **kwargs):
    remote_url, *args = args
    local_filename, *_ = args if len(args) else None, 
    super().__init__(remote_url=remote_url, local_filename=local_filename)

    ## Supported protocols
    file_protocols = ('file://',)
    requests_protocols = ('https://', 'http://')

    if any([self.remote_url.startswith(p) for p in file_protocols]):
      self._file = remote_url[7:]
      if self.local_filename is not None:
        raise NotImplementedError("Copy from local file system unavailable") 

    elif any([self.remote_url.startswith(p) for p in requests_protocols]):
      if self.local_filename is not None:
        self._file = self.local_filename 
      else:
        h = hashlib.sha1()
        h.update(self.remote_url.encode('utf-8'))
        self._file = f"/tmp/lamarr.resource.{h.hexdigest()[:16]}"

    else:
      raise NotImplementedError(
          f"Protocol for {self.remote_url} unknown or not supported. "
          f"Supported protocols: {', '.join(file_protocols+requests_protocols)}"
          )


  ################################################################################
  ## Handles implicit conversion from a string representing a url
  ## 

  @classmethod
  def __get_validators__ (cls):
    yield cls.validate

  @classmethod 
  def validate (cls, v):
    if isinstance(v, RemoteResource):
      return RemoteResource
    elif isinstance(v, str):
      return RemoteResource(v)
    elif isinstance(v, dict):
      if 'remote_url' in v.keys() and 'local_filename' in v.keys():
        return RemoteResource(
            remote_url=v['remote_url'],
            local_filename=v['local_filename']
            )

    raise ValueError(f"Unexpected initializer {v} for RemoteResource")

  def download (self, force: bool = False):
    if os.path.exists(self._file) and not force:
      return self

    logger = logging.getLogger(self.__class__.__name__)
    logger.info(f"Downloading {self.remote_url} to {self._file}")

    res = requests.get(self.remote_url, allow_redirects=True)
    res.raise_for_status()

    with open(self._file, 'wb') as f:
      f.write(res.content)

    return self

  @property 
  def file (self):
    self.download(force=False)
    logger = logging.getLogger(self.__class__.__name__)
    logger.debug(f"Accessing {self._file} as cached version of {self.remote_url}")
    return self._file


if __name__ == '__main__':
  pvdb = RemoteResource("https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/PrimaryVertex/PrimaryVertexSmearing.db")
  print (pvdb.download(force=True).file)
  pvdb2 = RemoteResource(f"file://{pvdb.file}")
  print (pvdb2._file)
  print (pvdb2.file)

  try:
    RemoteResource("ahahah://just-kidding.com")
  except NotImplementedError:
    pass
  else:
    assert False, "Failed raising exception on bad protocol"
  
