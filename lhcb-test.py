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

data_pkg = "https://github.com/LamarrSim/SQLamarr/raw/master/temporary_data" 
pvdb = PyLamarr.RemoteResource(f"{data_pkg}/PrimaryVertex/PrimaryVertexSmearing.db")

pipeline = LHCb.BasePipeline([
    ('PVFinder', PyLamarr.PVFinder),
    ('MCParticleMaker', PyLamarr.MCParticleSelector),
    ('PVReco', LHCb.PVReconstruction(condition='2016_pp_MagUp')),
    ('TrkAcc', LHCb.Tracking.Acceptance()),
    ('TrkEff', LHCb.Tracking.Efficiency()),
    ('TrkAssign', LHCb.Tracking.AssignCategory()),
    ('Propagate2CTB', LHCb.Tracking.PropagateToClosestToBeam()),
    ('TrkResolution', LHCb.Tracking.Resolution()),
    ('TrkCovariance', LHCb.Tracking.Covariance()),
    *LHCb.ParticleID.configure_pipeline(), 
    ('PrintStats', print_stats),
    ],
    batch=5,
    )

from glob import glob
filenames = glob("../SQLamarr/temporary_data/HepMC2-ascii/DSt_Pi.hepmc2/evt*.mc2")
load_args = zip(filenames, [1]*len(filenames), range(len(filenames)))

#pipeline.execute(list(load_args), thread_id=0)
with open("pipeline.xml", "w") as f:
  pipeline.to_xml(f)

with open("pipeline.xml") as f:
  reloaded = LHCb.BasePipeline.read_xml(f)

reloaded.sequence.append(("PrintStats", print_stats))
print (reloaded.sequence)
reloaded.execute(list(load_args), thread_id=0)

