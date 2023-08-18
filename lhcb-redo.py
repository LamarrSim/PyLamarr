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
  df = pd.read_sql_query("SELECT * FROM pid", db)
  print (df)

loader = PyLamarr.loaders.UprootLoader(
            "/mlinfn/shared/lamarr/anderlinil/test_data/LamarrExample-100kev.root",
            tables=('DataSources', 'MCParticles', 'MCVertices')
        )

pipeline = LHCb.BasePipeline([
    *LHCb.Tracking.configure_pipeline(),
    #*LHCb.ParticleID.configure_pipeline(), 
    ('PrintStats', print_stats),
    ],
    loader=loader,
    )

pipeline.execute(loader.batches[:10], thread_id=0)


