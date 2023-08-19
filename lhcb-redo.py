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

loader = PyLamarr.loaders.UprootLoader(
            "/pclhcb06/landerli/LamarrOnGaussino/lhcb-gaussino/Today/Gaussino/LamarrExample-1kev.root",
            tables=('MCVertices', 'DataSources', 'MCParticles', 'GenVertices', 'GenParticles'),
        )
collector = PyLamarr.collectors.PandasCollector((
    'MCParticles',
    'MCVertices',
    'tmp_particles_recoed_as',
    'tmp_resolution_out',
    'particles',
    'covariance',
    'pid',
    'GenParticles',
    'GenVertices'))

validator = EDM4hepValidator()

n_batches = 3
from tqdm import tqdm
with tqdm(total=n_batches) as progress_bar:
  pipeline = LHCb.BasePipeline([
      *LHCb.Tracking.configure_pipeline(),
      *LHCb.ParticleID.configure_pipeline(library="file:///pclhcb06/mabarbet/PythonFastSim/exports/lb-pidsim-train/compiledmodel_2016-MagUp-sim.so"), 
      #('PrintStats', print_stats),
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
    





