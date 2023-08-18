#!/bin/env python3 

import sys
sys.path.append("../SQLamarr/python")

from argparse import ArgumentParser
import PyLamarr
import logging
import time

import pandas as pd 

from PyLamarr import LHCb


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
            "/pclhcb06/landerli/LamarrOnGaussino/lhcb-gaussino/Today/Gaussino/LamarrExample-100kev.root",
            tables=('MCVertices', 'DataSources', 'MCParticles'),
            max_rows = 10000
        )
collector = PyLamarr.collectors.PandasCollector(('MCParticles', 'MCVertices', 'tmp_particles_recoed_as', 'tmp_resolution_out', 'particles', 'covariance', 'pid'))

n_batches = 10000
from tqdm import tqdm
with tqdm(total=n_batches) as progress_bar:
  pipeline = LHCb.BasePipeline([
      *LHCb.Tracking.configure_pipeline(),
      *LHCb.ParticleID.configure_pipeline(), 
      #('PrintStats', print_stats),
      ('UpdateTQDM', PyLamarr.function (lambda db: progress_bar.update(1))),
      ('Collector', collector),
      ],
      loader=loader,
      )

  pipeline.execute(loader.batches[:n_batches], thread_id=0)


import sqlite3 as sql
import os
if os.path.exists("redo-lhcb-out.db"):
  os.remove("redo-lhcb-out.db")

with sql.connect("redo-lhcb-out.db") as db:
  for key, table in collector.dataframe.items():
    table.to_sql(key, db, index=False)
    





