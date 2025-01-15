import os
import logging
import hashlib

from pydantic import BaseModel, PrivateAttr, validator
from typing import Optional

import requests


class RemoteResource (BaseModel):
    """Resource on the Internet, locally cached.
  
    # Remote Resource mechanism

    Most of the parametrizations Lamarr relies on are committed and maintained in
    remote repositories. The PyLamarr.RemoteResource class implements a simple
    caching mechanism to download the remote parametrizations on demand in case they
    are not available locally. A hash of the URL identifying the remote resource is
    used to represent the local cache of the remote resource.
    Note that in case the remote resource is updated without modifying its URL,
    the local cache is not automatically updated.


    ### Example.
    Consider the file `PrimaryVertexSmearing.db` encoding the parametrizations for
    Primary Vertex reconstruction, and made available publicly here:
    `https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/PrimaryVertex/PrimaryVertexSmearing.db`

    The following snippet of code enables caching the file locally:
    ```python
    from PyLamarr import RemoteResource
    url = ("https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
           "PrimaryVertex/PrimaryVertexSmearing.db")

    pv_params = RemoteResource(url)

    # Now the file might not be available locally, but a lazy download is triggered
    # when accessing its path:

    import sqlite3
    with sqlite3.connect(pv_params.file) as db:
        # ... do something ...
    ```

    Now, in case the remote file is updated, it may be necessary to download the
    updated version. This can be achieved forcing the download with:
    ```python
    pv_params.download(force=True)
    ```

    or, replacing the connection attempt in the previous example:
    ```python
    import sqlite3
    with sqlite3.connect(pv_params.download(force=True).file) as db:
        # ... do something ...
    ```


    ### Accessing local resources
    A local resourcce can be encapsulated inside `RemoteResource` which is
    the expected format for most of the parametrization test_data in `PyLamarr`.

    For example, if testing your local version of `MyPrimaryVertexSmearing.db`,
    you can write
    ```python
    pv_params = RemoteResource("file://MyPrimaryVertexSmearing.db")

    # Now the file might not be available locally, but a lazy download is triggered
    # when accessing its path:

    import sqlite3
    with sqlite3.connect(pv_params.file) as db:
        #...
    ```

    Note, however, that forcing the download of a local resource would raise an
    Exception.


    ### Implicit conversion from URL
    Most of the parametrizations relying on external dependencies expect an
    instance of `RemoteResource` identifying the file to obtain the parametrization
    from. An implicit cast from string to `RemoteResource` enables passing directly
    a string with a URL (possibly pointing to a local file), which gets
    transparently converted into a `RemoteResource` instance and used in the file.
    """
    remote_url: str
    local_filename: Optional[str] = None
    _file: Optional[str] = PrivateAttr()

    def __init__ (self, *args, **kwargs):
        """@private Constructor performing input validation"""
        remote_url, *args = args
        local_filename, *args = args if len(args) else None,
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

    # Handles implicit conversion from a string representing an url
    @classmethod
    def __get_validators__ (cls):
        """@private Get validators for implicit casting from URL by pydantic"""
        yield cls.validate

    @classmethod
    def validate (cls, v):
        """@private Implement implicit casting"""
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
        """Download the remote resource is not available locally or if forced.
        Can raise an exception if the download fails or upon attempts of downloading
        local resources (represented by protocol `file://`)

        @param force: Force the download of the remote resource independently of
          the cache availability

        @return Updated instance of `RemoteResource` (`self`)
        """

        if os.path.exists(self._file) and not force:
            return self

        if self.remote_url.startswith("file://"):
            raise FileNotFoundError(f"File {self._file} not found.")

        logger = logging.getLogger(self.__class__.__name__)
        logger.info(f"Downloading {self.remote_url} to {self._file}")

        res = requests.get(self.remote_url, allow_redirects=True)
        res.raise_for_status()

        with open(self._file, 'wb') as f:
            f.write(res.content)

        return self

    @property
    def file (self):
        """@property Access the local file **path** downloading it if necessary."""
        self.download(force=False)
        logger = logging.getLogger(self.__class__.__name__)
        logger.debug(f"Accessing {self._file} as cached version of {self.remote_url}")
        return self._file


if __name__ == '__main__':
    pvdb = RemoteResource(
        "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/PrimaryVertex/PrimaryVertexSmearing.db"
    )
    print(pvdb.download(force=True).file)
    pvdb2 = RemoteResource(f"file://{pvdb.file}")
    print(pvdb2._file)
    print(pvdb2.file)

    try:
        RemoteResource("ahahah://just-kidding.com")
    except NotImplementedError:
        pass
    else:
        assert False, "Failed raising exception on bad protocol"
