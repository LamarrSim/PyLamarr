import os
import logging
import hashlib

import requests

class RemoteResource:
  def __init__ (self, 
      remote_url: str, 
      local_filename: str = None, 
      ):
    self._url = remote_url
    self.logger = logging.getLogger(self.__class__.__name__)

    ## Supported protocols
    file_protocols = ('file://',)
    requests_protocols = ('https://', 'http://')

    if any([remote_url.startswith(p) for p in file_protocols]):
      self._file = remote_url[7:]
      if local_filename is not None:
        raise NotImplementedError("Copy from local file system unavailable") 

    elif any([remote_url.startswith(p) for p in requests_protocols]):
      if local_filename is not None:
        self._file = local_filename 
      else:
        h = hashlib.sha1()
        h.update(remote_url.encode('utf-8'))
        self._file = f"/tmp/lamarr.resource.{h.hexdigest()[:16]}"

    else:
      raise NotImplementedError(
          f"Protocol for {self._url} unknown or not supported. "
          f"Supported protocols: {', '.join(file_protocols+requests_protocols)}"
          )

  def download (self, force: bool = False):
    if os.path.exists(self._file) and not force:
      return self

    self.logger.info(f"Downloading {self._url} to {self._file}")

    res = requests.get(self._url, allow_redirects=True)
    res.raise_for_status()

    with open(self._file, 'wb') as f:
      f.write(res.content)

    return self

  @property 
  def file (self):
    self.download(force=False)
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
  
