#!/bin/env python3 

import sys
sys.path.append("../SQLamarr/python")

from argparse import ArgumentParser
import PyLamarr
import logging
import time

import pandas as pd 

from PyLamarr import LHCb
from PyLamarr.validators import EDM4hepValidator


parser = ArgumentParser()
parser.add_argument("--verbose", "-v", action="store_true")
parser.add_argument("--veryverbose", "-V", action="store_true")

args = parser.parse_args()

if args.verbose:
  PyLamarr.configure_logger(level=logging.INFO)
if args.veryverbose:
  PyLamarr.configure_logger(level=-1)

################################################################################
@PyLamarr.function
def print_stats (db):
  df = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type == 'table'", db)
  print (df)
  print(pd.read_sql_query("SELECT COUNT(*) AS numberOfTracks FROM Track", db))

loader = PyLamarr.loaders.UprootLoader(
            "/home/shared/lamarr/anderlinil/PyLamarr/LamarrExample.root",
            tables=('MCVertices', 'DataSources', 'MCParticles', 'GenVertices', 'GenParticles', 'GenEvents'),
        )

collector = PyLamarr.collectors.PandasCollector((
    'EventHeader',
    'MCParticle',
    'MCParticles',
    'MCVertices',
    'ReconstructedParticle',
    'ParticleID',
    'MCVertex',
    'Vertex',
    'GenParticles',
    'GenVertices',
    'particles',
    'covariance',
    'pid',
    'Track',
    'LHCbTrackState',
    ))

validator = EDM4hepValidator()

PID_MODEL=PyLamarr.RemoteResource(
  "file:///home/minio/anderlinil/models/PID_sim10-2016MU_latest_v1.so"
  )

n_batches = 100#0
from tqdm import tqdm
with tqdm(total=n_batches) as progress_bar:
  pipeline = LHCb.BasePipeline([
      ('PVReco', LHCb.PVReconstruction(condition='2016_pp_MagUp')),
      *LHCb.Tracking.configure_pipeline(),
      *LHCb.ParticleID.configure_pipeline(library=PID_MODEL), 
      *LHCb.EDM4hep.configure_pipeline(), 
#      ('PrintStats', print_stats),
      ('UpdateTQDM', PyLamarr.function (lambda db: progress_bar.update(1))),
      ('Validator', validator),
      ('Collector', collector),
      ],
      loader=loader,
      )

  pipeline.execute(loader.batches[:n_batches], thread_id=0)

print (validator.summary())


import sqlite3 as sql
import os
if os.path.exists("redo-lhcb-out.db"):
  os.remove("redo-lhcb-out.db")

with sql.connect("redo-lhcb-out.db") as db:
  for key, table in collector.dataframe.items():
    table.to_sql(key, db, index=False)
    

#with open("test-pipeline.xml", "w") as f:
#  pipeline.to_xml(f)

