#!/bin/env python3 
import IPython


import sys
sys.path.append("../SQLamarr/python")

from argparse import ArgumentParser
import PyLamarr
import logging
import time
import random

import pandas as pd 
import shutil, os

from PyLamarr import LHCb
import tarfile

parser = ArgumentParser()
parser.add_argument("--verbose", "-v", action="store_true")
parser.add_argument("--veryverbose", "-V", action="store_true")
parser.add_argument("--output", "-o", default="pylamarr-output.db")
parser.add_argument("--jobid", "-j", type=int, default=random.randint(0, 100000))
parser.add_argument("tarfiles", help="bz2.tar archive with .hepmc2 files to analyze", nargs='+')

args = parser.parse_args()

if args.verbose:
  PyLamarr.configure_logger(level=logging.INFO)
if args.veryverbose:
  PyLamarr.configure_logger(level=-1)

from glob import glob
tarfiles = sum([glob(path) for path in args.tarfiles], [])
if len(tarfiles) == 0:
  raise RuntimeError(f"No file matches {' or '.join(args.tarfiles)}")
print (tarfiles)

################################################################################
@PyLamarr.function
def print_stats (db):
  df = pd.read_sql_query("SELECT * FROM ClusterInfo LIMIT 5;", db)
  print (df)

data_pkg = "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data" 
pvdb = PyLamarr.RemoteResource(f"{data_pkg}/PrimaryVertex/PrimaryVertexSmearing.db")

from PyLamarr.validators import EDM4hepValidator
validator = EDM4hepValidator()

from glob import glob
#filenames = glob("../SQLamarr/temporary_data/HepMC2-ascii/DSt_Pi.hepmc2/evt*.mc2")
#load_args = zip(filenames, [1]*len(filenames), range(len(filenames)))

batch_size = 1

loader = PyLamarr.loaders.CompressedHepMCLoader(max_event=None)

collector = PyLamarr.collectors.PandasCollector((
    'EventHeader',
    'MCParticle',
    'MCParticles',
    'MCVertices',
    'RecSummary',
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
    'MCParticle__parents__MCParticle',
    'Cluster',
    'ClusterInfo',
    ))

PID_MODEL=PyLamarr.RemoteResource(
  "file:///home/minio/anderlinil/models/PID_sim10-2016MU_latest_v1.so"
  )

from tqdm import tqdm
from math import ceil
with tqdm(total=ceil(len(tarfiles)/batch_size)) as progress_bar:
  pipeline = LHCb.BasePipeline([
      ('PVFinder', PyLamarr.PVFinder),
      ('MCParticleMaker', PyLamarr.MCParticleSelector),
      ('PVReco', LHCb.PVReconstruction(condition='2016_pp_MagUp')),
      ('RecSummary', LHCb.RecSummaryMaker()),
      *LHCb.Tracking.configure_pipeline(),
      *LHCb.ParticleID.configure_pipeline(library=PID_MODEL), 
      *LHCb.EDM4hep.configure_pipeline(), 
      # ('PrintStats', print_stats),
      *LHCb.Photons.configure_pipeline(), 
      #('StopThink', PyLamarr.function(lambda db: IPython.embed())),
      ('UpdateTQDM', PyLamarr.function (lambda db: progress_bar.update(1))),
      ('Validator', validator),
      ('Collector', collector),
    ],
    loader=loader,
    batch=batch_size,
    )

  pipeline.execute(tarfiles, thread_id=args.jobid)

import sqlite3 as sql
import os
if os.path.exists(args.output):
  os.remove(args.output)

tmp_file = f"/tmp/lamarr.tmp.{args.jobid}.{random.randint(0, 100000)}.db"
try:
  logging.getLogger("main").info(f"Serializing the output to SQLite {tmp_file}")
  with sql.connect(tmp_file) as db:
    for key, table in collector.dataframe.items():
      table.to_sql(key, db, index=False)
  shutil.copy(tmp_file, args.output)
finally:
  if os.path.exists(tmp_file):
    os.remove(tmp_file)

#pipeline.execute(list(load_args), thread_id=0)
#with open("pipeline.xml", "w") as f:
#  pipeline.to_xml(f)

#with open("pipeline.xml") as f:
#  reloaded = LHCb.BasePipeline.read_xml(f)


#reloaded.sequence.append(("PrintStats", print_stats))
#print (reloaded.sequence)

