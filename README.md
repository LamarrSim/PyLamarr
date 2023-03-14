# PyLamarr
PyLamarr is a pure-python package describing the LHCb Simulation pipeline
combining C++ algorithms defined in `SQLamarr` and contains mostly
configurations.

In the future, the same configurations might be exported (or read directly)
from Gaudi and Gaussino to deploy the SQLamarr building blocks in a dedicated
Gaudi algorithm.

## Remote resources
The Gaudi application relies on `cvmfs` to distribute the parametrizations.
`PyLamarr` is intended to be less dependent on CERN-related system
configurations to be easily deployed in virtual environments or public services
(such as Google Colab).
Remote configurations are accessed by PyLamarr via `http` or `https` protocols,
caching the remote file locally to avoid unnecessary traffic.

Please refer to the documentation of `PyLamarr.RemoteResource.RemoteResource` for
implementation details.

## License
PyLamarr is released under MIT License.
Note, however, that SQLamarr, PyLamarr depends on, is released under GPL-3
licence with copyright owned by CERN.
