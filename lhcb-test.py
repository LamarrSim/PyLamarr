#!/bin/env python3
import IPython

from tqdm import tqdm
from math import ceil

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
parser.add_argument(
  "--tracking-model",
  default="https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
          "models/lhcb.trk.2016MU.20230128.so",
  help="Compiled model with tracking parametrizations",
)
parser.add_argument(
  "--pid-model",
  default="https://gitlab.cern.ch/lhcb-datapkg/LamarrData/-/raw/v3r0/data/"
          "ChargedPID/2016/compiledmodel_2016-MagUp-sim.so?inline=false",
  help="Compiled model with tracking parametrizations",
)
parser.add_argument(
    "--ecal-efficiency-model",
    default=None,
    help="Keras2 model for the ECAL efficiency (local directory path)"
)

parser.add_argument(
    "--ecal-resolution-model",
    default=None,
    help="Keras2 model for the ECAL resolution (local directory path)"
)

parser.add_argument(
  "--pv-model",
  default="https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data/"
          "PrimaryVertex/PrimaryVertexSmearing.db",
  help="Compiled model with tracking parametrizations",
)

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

pvdb = PyLamarr.RemoteResource(args.pv_model)
tracking_model = PyLamarr.RemoteResource(args.tracking_model)
pid_model = PyLamarr.RemoteResource(args.pid_model)

# from PyLamarr.validators import EDM4hepValidator
# validator = EDM4hepValidator()

from glob import glob
#filenames = glob("../SQLamarr/temporary_data/HepMC2-ascii/DSt_Pi.hepmc2/evt*.mc2")
#load_args = zip(filenames, [1]*len(filenames), range(len(filenames)))

batch_size = 1

loader = PyLamarr.loaders.CompressedHepMCLoader(max_event=None, events_per_batch=10)

collector = PyLamarr.collectors.PandasCollector([
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
        ])



with tqdm(total=ceil(len(tarfiles)/batch_size)) as progress_bar:
    pipeline = LHCb.BasePipeline([
        ('PVFinder', PyLamarr.PVFinder),
        ('MCParticleMaker', PyLamarr.MCParticleSelector),
        ('PVReco', LHCb.PVReconstruction(condition='2016_pp_MagUp', library=pvdb)),
        ('RecSummary', LHCb.RecSummaryMaker()),
        *LHCb.Tracking.configure_pipeline(library=tracking_model),
        *LHCb.ParticleID.configure_pipeline(library=pid_model),
        *LHCb.EDM4hep.configure_pipeline(),
        # *LHCb.ParticleID.configure_pipeline(),
        # ('PrintStats', print_stats),
        *LHCb.Photons.configure_pipeline(
            efficiency_model=args.ecal_efficiency_model,
            resolution_model=args.ecal_resolution_model
        ),
        #('StopThink', PyLamarr.function(lambda db: IPython.embed())),
        ('UpdateTQDM', PyLamarr.function (lambda db: progress_bar.update(1))),
        #('Validator', validator),
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
            table.to_sql(key, db, index=False, chunksize=10000)
    shutil.copy(tmp_file, args.output)
finally:
    if os.path.exists(tmp_file):
        os.remove(tmp_file)

