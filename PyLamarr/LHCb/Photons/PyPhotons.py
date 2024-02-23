import numpy                as np 
import pandas as pd 
import tensorflow as tf

import PyLamarr
import pickle

import IPython

from pathlib import Path
EFFICIENCY_MODEL = Path("/lbpool/lhcb0/mabarbet/models/Ecal_efficiency_photon_models/")
EFFICIENCY_MODEL_VERSION = "20240120-11h56m21s_Ecal_efficiency_photon_2016MU_ann"
SMEARING_MODEL = Path("/lbpool/lhcb0/mabarbet/models/Ecal_resolution_id_photon_models/")
SMEARING_MODEL_VERSION= "20240120-00h09m55s_Ecal_resolution_id_photon_2016MU_gan"
# SMEARING_MODEL_VERSION = "20240120-03h18m19s_Ecal_resolution_id_photon_2016MU_gan"

tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)



def invertColumnTransformer(column_transformer, preprocessed_X):
    from sklearn.compose import ColumnTransformer
    assert isinstance(column_transformer, ColumnTransformer)

    iCol = 0
    postprocessed_split = dict()
    for name, algo, cols in column_transformer.transformers_:
        preprocessed_cols = list()
        for _ in range(len(cols)):
            preprocessed_cols.append(preprocessed_X[:, iCol][:, None])
            iCol += 1
        preprocessed_block = np.concatenate(preprocessed_cols, axis=1)
        if algo == "passthrough":
            postprocessed_split[name] = preprocessed_block
        else:
            postprocessed_split[name] = algo.inverse_transform(preprocessed_block)

    X = [None] * preprocessed_X.shape[1]
    for name, _, cols in column_transformer.transformers_:
        for i, iCol in enumerate(cols):
            X[iCol] = postprocessed_split[name][:, i][:, None]

    return np.concatenate(X, axis=1)


def _eval_efficiency(X):
  efficiency_model = tf.keras.models.load_model(EFFICIENCY_MODEL/EFFICIENCY_MODEL_VERSION)
  with open(EFFICIENCY_MODEL / 'tX_2016MU.pkl', 'rb') as tx_file:
    tX = pickle.load(tx_file)

  y_hat = efficiency_model.predict(tX.transform(X), batch_size=10000, verbose=0)

  return y_hat 
    

def _eval_smearing(X):
  smearing_model = tf.keras.models.load_model(SMEARING_MODEL/SMEARING_MODEL_VERSION)
  with open(SMEARING_MODEL / 'tX_2016MU.pkl', 'rb') as tx_file:
    tX = pickle.load(tx_file)

  with open(SMEARING_MODEL / 'tY_2016MU.pkl', 'rb') as ty_file:
    tY = pickle.load(ty_file)

  prep_x = tX.transform(X)
  n_entries, _ = X.shape
  prep_y_hat = smearing_model.predict(
      np.c_[prep_x, np.random.normal(0, 1, (n_entries, 64))],
      verbose=0,
      batch_size=10000
      )

  ret = invertColumnTransformer(tY, prep_y_hat)
  return ret



    

@PyLamarr.function
def PyPhotons(db):
  gen_photons = pd.read_sql_query("""
      SELECT gev.datasource_id AS event_id, p.*, v.*
      FROM MCParticles AS p
      JOIN MCVertices AS v 
        ON p.production_vertex == v.mcvertex_id
           AND p.genevent_id == v.genevent_id
      JOIN GenEvents AS gev
        ON gev.genevent_id = p.genevent_id 
      WHERE 
          pid = 22 
        AND 
          p.pe > 1000
        AND 
          abs(v.x) < 200
        AND 
          abs(v.y) < 200
        AND 
          abs(v.z) < 2000
      """, db)

  event_id = gen_photons.event_id.values
  mcparticle_id = gen_photons.mcparticle_id.values
  ovx, ovy, ovz = gen_photons[['x', 'y', 'z']].values.T
  e, px, py, pz = gen_photons[['pe', 'px', 'py', 'pz']].values.T

  tx = px/pz
  ty = py/pz

  ecal_z = 12689. # mm
  ecal_x = ovx + tx * (ecal_z - ovz)
  ecal_y = ovy + ty * (ecal_z - ovz)

  mask = (
    (ecal_x > -4e3) & (ecal_x < 4e3) &
    (ecal_y > -4e3) & (ecal_y < 4e3) &
    (tx > -0.35) & (tx < 0.35) &
    (ty > -0.25) & (ty < 0.25) &
    (pz > 0) & (pz < 200e3)
    )

  X_eff = np.c_[ecal_x, ecal_y, np.log(e/1e3), tx, ty, ovx, ovy, ovz, np.zeros_like(ecal_x)]

  efficiency = _eval_efficiency(X_eff)
  r = np.random.uniform(0, 1, len(X_eff))

  ceff = np.cumsum(efficiency, 1)
  eff_as_photon = r < ceff[:,0]
  eff_as_photon_from_pi0 = (r > ceff[:,0]) & (r < ceff[:,1])

  X_res = np.c_[ecal_x, ecal_y, np.log(e/1e3), tx, ty, ovx, ovy, ovz, np.zeros_like(ecal_x), eff_as_photon, eff_as_photon_from_pi0]
  dx, dy, de_rel, reco_PhotonID, reco_IsNotE, reco_IsNotH = _eval_smearing(X_res).T 

  sigma_x = np.sqrt(np.exp(-1.65 * np.log(e) + 17.0))
  sigma_y = np.sqrt(np.exp(-1.65 * np.log(e) + 17.0))
  sigma_e = np.sqrt(np.exp(0.89 * np.log(e) + 5.1))

  IPython.embed()


  clusters = pd.DataFrame(dict(
    mask=mask & eff_as_photon,
    event_id=event_id,
    type=np.full_like(mcparticle_id, 4),
    calocluster_id = mcparticle_id,
    center_x = ecal_x,# + dx,  #np.random.normal(ecal_x, sigma_x),
    center_y = ecal_y,# + dy,  #np.random.normal(ecal_y, sigma_y),
    z = ecal_z,
    # energy = e * (1. + de_rel),  
    energy = np.random.normal(e, sigma_e),
    cov_xx = sigma_x * sigma_x,
    cov_yy = sigma_y * sigma_y,
    cov_ee = sigma_e * sigma_e,
  )).query("mask").drop(columns=['mask'])

  clusters.to_sql("Cluster", db, if_exists='replace')

  cluster_info = pd.concat([
    pd.DataFrame(dict(
      mask=eff_as_photon,
      event_id=event_id,
      calocluster_id=mcparticle_id,
      info_key=np.full_like(mcparticle_id, info_key),
      info_value=info_value
    )).query("mask").drop(columns=['mask'])
    for info_key, info_value in [
        (383, reco_IsNotH),
        (382, reco_IsNotE),
        (380, reco_PhotonID),
        # These magic numbers come from https://lhcb-doxygen.web.cern.ch/lhcb-doxygen/davinci/v50r5/d2/d57/class_l_h_cb_1_1_proto_particle.html
      ]
    ]).sort_values('calocluster_id', ignore_index=True)

  cluster_info.to_sql("ClusterInfo", db, if_exists='replace')

