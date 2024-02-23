from PyLamarr.Concatenate import Concatenate

## Local imports 
from .GanPipeline import GanPipeline
from .IsMuonEfficiency import IsMuonEfficiency as IsMuonEff
from .AssignIsMuon import AssignIsMuon


def concat_outputs (name, algos):
  output_tabs = [p.output_table for p in algos]

  columns = set.intersection(*[
    set(alg.output_columns).union(set(alg.references))
    for alg in algos])

  return f"Concat{name.capitalize()}", Concatenate(name, output_tabs, columns)


def configure_pipeline(library: str):
  ismuon_pipeline = [
      ('MuIsMuonEff', IsMuonEff(library, 'isMuon_muon_pipe', 'tmp_ismuon_mu', 13)),
      ('PiIsMuonEff', IsMuonEff(library, 'isMuon_pion_pipe', 'tmp_ismuon_pi', 211)),
      ('KIsMuonEff', IsMuonEff(library, 'isMuon_kaon_pipe', 'tmp_ismuon_k', 321)),
      ('PIsMuonEff', IsMuonEff(library, 'isMuon_proton_pipe', 'tmp_ismuon_p', 2212)),
      ]
  ismuon_pipeline.append(concat_outputs('ismuoneff', [a for _, a in ismuon_pipeline]))
  ismuon_pipeline.append(('AssignIsMuon', AssignIsMuon('ismuoneff')))
  ismuon_tab = ismuon_pipeline[-1][1].output_table

  gan_pipeline = [
    ("MuonPidPipe", 
      GanPipeline(library, "full_muon_pipe", "tmp_pid_mu", 13, ismuon_tab)),
    ("PionPidPipe", 
      GanPipeline(library, "full_pion_pipe", "tmp_pid_pi", 211, ismuon_tab)),
    ("KaonPidPipe", 
      GanPipeline(library, "full_kaon_pipe", "tmp_pid_k", 321, ismuon_tab)),
    ("ProtonPidPipe", 
      GanPipeline(library, "full_proton_pipe", "tmp_pid_p", 2212, ismuon_tab)),
  ]
  gan_pipeline.append(concat_outputs('pid', [a for _, a in gan_pipeline]))

  return ismuon_pipeline + gan_pipeline


