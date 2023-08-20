import PyLamarr
from particle import Particle


@PyLamarr.persistent_table((
    'eventNumber', 'runNumber', 'timeStamp', 'weight'
))
def EventHeader():
    """
      Event Header. Additional parameters are assumed to go into the metadata tree.
    """
    return "SELECT evt_number, run_number, 0, 0 FROM DataSources;"


@PyLamarr.persistent_table((
    "mcparticle_id",
    "PDG",
    "generatorStatus",
    "simulatorStatus",
    "charge",
    "time",
    "mass",
    "vertex_x",
    "vertex_y",
    "vertex_z",
    "endpoint_x",
    "endpoint_y",
    "endpoint_z",
    "momentum_x",
    "momentum_y",
    "momentum_z",
#    "momentumAtEndpoint_x",
#    "momentumAtEndpoint_y",
#    "momentumAtEndpoint_z",
#    "spin_x",
#    "spin_y",
#    "spin_z",
#    "colorFlow_x",
#    "colorFlow_y",
#    "colorFlow_z",
))
def MCParticle():
    """
    The Monte Carlo particle - based on the lcio::MCParticle.
    """
    return """
    SELECT
      mcp.mcparticle_id           AS mcparticle_id,
      mcp.pid                     AS pdg,
      gp.status                   AS generator_status,
      mcp.is_signal               AS simulator_status,
      propagation_charge(mcp.pid) AS charge,
      ov.t                        AS time,
      mcp.m                       AS mass,
      ov.x                        AS vertex_x,
      ov.y                        AS vertex_y,
      ov.z                        AS vertex_z,
      end.x                       AS endpoint_x,
      end.y                       AS endpoint_y,
      end.z                       AS endpoint_z,
      mcp.px                      AS momentum_x,
      mcp.py                      AS momentum_y,
      mcp.pz                      AS momentum_z
    FROM MCParticles AS mcp
    LEFT JOIN GenParticles AS gp
      ON mcp.genparticle_id == gp.genparticle_id
    LEFT JOIN GenVertices AS ov
      ON gp.production_vertex == ov.genvertex_id
    LEFT JOIN GenVertices AS end
      ON gp.end_vertex == end.genvertex_id
    """


@PyLamarr.persistent_table(('daughter', 'parent'))
def MCParticle__parents__MCParticle():
    """
    Zip table from parent to daughter
    """
    return """
    SELECT
      mcp.mcparticle_id AS daughter,
      parent.mcparticle_id AS parent
    FROM MCParticles AS mcp
    LEFT JOIN GenParticles AS daughter_gp
      ON mcp.genparticle_id == daughter_gp.genparticle_id
    INNER JOIN GenParticles AS parent_gp
      ON parent_gp.end_vertex == daughter_gp.production_vertex
    LEFT JOIN MCParticles AS parent
      ON parent.genparticle_id == parent_gp.genparticle_id
    """


@PyLamarr.persistent_table(('parent', 'daughter'))
def MCParticle__daughters__MCParticle():
    """
    Zip table from daughter to parent
    """
    return """
    SELECT
      mcp.mcparticle_id AS parent,
      daughter.mcparticle_id AS daughter
    FROM MCParticles AS mcp
    LEFT JOIN GenParticles AS parent_gp
      ON mcp.genparticle_id == parent_gp.genparticle_id
    INNER JOIN GenParticles AS daughter_gp
      ON daughter_gp.end_vertex == parent_gp.production_vertex
    LEFT JOIN MCParticles AS daughter
      ON daughter.genparticle_id == daughter_gp.genparticle_id
    """


@PyLamarr.persistent_table((
  'particle_id', 'type', 'PDG', 'algorithmType', 'likelihood'
  ))
def ParticleID():
  """
  Particle Identification algorithms.
  - particle_id: index of the Particle table
  - algorithmType:
     - 0: boolean (e.g. isMuon)
     - 1: efficiency (e.g. isMuonEfficiency)
     - 2: log-likelihood (e.g. RichDLL or Global DLL)
     - 3: classifier (e.g. ProbNN)
  - type (unit digit is reserved for future additional versions):
     -   0: isMuonEff
     -  10: isMuon
     -  20: RichDLL
     -  30: MuonLL
     - 100: CombinedDLL wrt pion hypothesis
     - 110: ProbNN
  """
  return [
    "SELECT mcparticle_id,   0,  13, 0, ismuoneff FROM tmp_is_muon",
    "SELECT mcparticle_id,  10,  13, 1, is_muon FROM tmp_is_muon",
    "SELECT mcparticle_id,  20,   11, 2, RichDLLe    FROM pid",
    "SELECT mcparticle_id,  20,   13, 2, RichDLLmu   FROM pid",
    "SELECT mcparticle_id,  20,  211, 2, 0           FROM pid",
    "SELECT mcparticle_id,  20,  321, 2, RichDLLK    FROM pid",
    "SELECT mcparticle_id,  20, 2212, 2, RichDLLp    FROM pid",
    "SELECT mcparticle_id,  30,   13, 2, MuonMuLL    FROM pid",
    "SELECT mcparticle_id,  30, 2212, 2, MuonBkgLL   FROM pid",
    "SELECT mcparticle_id, 100,   11, 2, PIDe        FROM pid",
    "SELECT mcparticle_id, 100,   13, 2, PIDmu       FROM pid",
    "SELECT mcparticle_id, 100,  211, 2,  0          FROM pid",
    "SELECT mcparticle_id, 100,  321, 2, PIDK        FROM pid",
    "SELECT mcparticle_id, 100, 2212, 2, PIDp        FROM pid",
    "SELECT mcparticle_id, 110,   11, 2, ProbNNe     FROM pid",
    "SELECT mcparticle_id, 110,   13, 2, ProbNNmu    FROM pid",
    "SELECT mcparticle_id, 110,  211, 2, ProbNNpi    FROM pid",
    "SELECT mcparticle_id, 110,  321, 2, ProbNNk     FROM pid",
    "SELECT mcparticle_id, 110, 2212, 2, ProbNNp     FROM pid",
    ]


@PyLamarr.persistent_table((
    'track_id', 'mcparticle_id', 'type', 'chi2', 'ndf', 'ghostProb',
    # 'dEdx', 'dEdxError', 'radiusOfInnermostHit',
  ))
def Track():
  """
  Reconstructed track, intended as a collection of track states.
  """
  return """
    SELECT
      reco.mcparticle_id AS track_id,
      reco.mcparticle_id AS mcparticle_id,
      reco.track_type AS track_type,
      res.chi2PerDoF * floor(res.nDoF_f), floor(res.nDoF_f), res.ghostProb
    FROM tmp_particles_recoed_as AS reco
    LEFT JOIN tmp_resolution_out AS res ON reco.mcparticle_id == res.mcparticle_id
    WHERE reco.track_type != 0
  """


@PyLamarr.persistent_table((
  'track_id',
  'location',
  # 'D0',   # transverse impact parameter
  # 'phi',    # azimuthal angle
  # 'omega', # signed curvature of the track
  # 'Z0',    # longitudinal impact parameter
  # 'tanLambda', #lambda is the dip anglie of the track in r-z
  # 'time',   # time of the track when reaching this location
  'referencePoint_x',
  'referencePoint_y',
  'referencePoint_z',
  'slope_x',
  'slope_y',
  'momentum',
  'covMatrix_00',
  'covMatrix_01',
  'covMatrix_02',
  'covMatrix_03',
  'covMatrix_04',
  'covMatrix_11',
  'covMatrix_12',
  'covMatrix_13',
  'covMatrix_14',
  'covMatrix_22',
  'covMatrix_23',
  'covMatrix_24',
  'covMatrix_33',
  'covMatrix_34',
  'covMatrix_44',
  ))
def LHCbTrackState():
  """
  TrackState encodes the knowledge of a track in a specific location.
  Location:
   - 0: AtOther
   - 1: AtIP
   - 2: AtFirstHit
   - 3: AtLastHist
   - 4: AtCalorimeter
   - 5: AtVertex
   - 5: LastLocation

   For LHCb, AtIP (1) is used to indicate ClosestToBeam.

   Given the different variables used to describe a track state in LHCb
   and in 4pi experiments, we redefine the TrackState
  """
  return """
  SELECT
    mcp.mcparticle_id,
    1 AS location,
    ctb.x + res.dx AS referencePoint_x,
    ctb.y + res.dy AS referencePoint_y,
    ctb.z + res.dz AS referencePoint_z,
    (mcp.px / mcp.pz) + res.dtx AS slope_x,
    (mcp.px / mcp.pz) + res.dty AS slope_y,
    norm2(mcp.px, mcp.py, mcp.pz) + res.dp AS momentum,
    cov.cov00,
    cov.cov01,
    cov.cov02,
    cov.cov03,
    cov.cov04,
    cov.cov11,
    cov.cov12,
    cov.cov13,
    cov.cov14,
    cov.cov22,
    cov.cov23,
    cov.cov24,
    cov.cov33,
    cov.cov34,
    cov.cov44
    FROM tmp_particles_recoed_as AS reco
    LEFT JOIN MCParticles AS mcp
      ON mcp.mcparticle_id == reco.mcparticle_id
    LEFT JOIN tmp_resolution_out AS res
      ON res.mcparticle_id == reco.mcparticle_id
    LEFT JOIN covariance AS cov
      ON cov.mcparticle_id == reco.mcparticle_id
    LEFT JOIN tmp_closest_to_beam AS ctb
      ON ctb.mcparticle_id == reco.mcparticle_id
    WHERE reco.track_type != 0

  """


@PyLamarr.persistent_table((
  'vertex_id',
  'is_primary',  ## N.B. 'primary' is a reserved keyword in SQL
  'time',
#  'chi2',
#  'probability',
  'position_x',
  'position_y',
  'position_z',
  'covMatrix_xx',
  'covMatrix_yx',
  'covMatrix_zx',
  'covMatrix_yy',
  'covMatrix_yz',
  'covMatrix_zz',
  ))
def Vertex():
  return """
    SELECT 
      mcvertex_id AS vertex_id,
      true AS is_primary,
      t AS time,
      x AS position_x,
      y AS position_y,
      z AS position_z,
      1/sigma_x/sigma_x AS cov_xx,
      0 AS cov_yx,
      0 AS cov_zx,
      1/sigma_y/sigma_y AS cov_yy,
      0 AS cov_zy,
      1/sigma_z/sigma_z AS cov_zz
    FROM Vertices
  """

@PyLamarr.persistent_table((
  'particle_id',
  'mcparticle_id',
  'PDG',
  'type',
  'energy',
  'momentum_x',
  'momentum_y',
  'momentum_z',
  'referencePoint_x',
  'referencePoint_y',
  'referencePoint_z',
  'charge',
  'mass',
  #'goodnessOfPID',
  #'covMatrix_pxpx',
  #'covMatrix_pypx',
  #'covMatrix_pzpx',
  #'covMatrix_pepx',
  #'covMatrix_pypy',
  #'covMatrix_pzpy',
  #'covMatrix_pepy',
  #'covMatrix_pzpz',
  #'covMatrix_pepz',
  #'covMatrix_pepe',
  #'startVertex',
  ))
def ReconstructedParticle():
  return [f"""
    SELECT
      NULL AS particle_id,
      mcp.mcparticle_id AS mcparticle_id,
      {pdg}*propagation_charge(mcp.pid) AS PDG,
      trk.type AS type,
      POW(
        POW({Particle.from_pdgid(pdg).mass},2) + 
        POW(norm2(mcp.px, mcp.py, mcp.pz) + res.dp, 2), 
        0.5) AS energy,
      slopes_to_cartesian(0,
          norm2(mcp.px, mcp.py, mcp.pz) + res.dp,
          mcp.px/mcp.pz + res.dp,
          mcp.py/mcp.pz + res.dp
          ) AS momentum_x,
      slopes_to_cartesian(1,
          norm2(mcp.px, mcp.py, mcp.pz) + res.dp,
          mcp.px/mcp.pz + res.dp,
          mcp.py/mcp.pz + res.dp
          ) AS momentum_y,
      slopes_to_cartesian(2, 
          norm2(mcp.px, mcp.py, mcp.pz) + res.dp,
          mcp.px/mcp.pz + res.dp,
          mcp.py/mcp.pz + res.dp
          ) AS momentum_z,
      ctb.x + res.dx AS referencePoint_x,
      ctb.y + res.dy AS referencePoint_y,
      ctb.z + res.dz AS referencePoint_z,
      propagation_charge(mcp.pid) AS charge,
      {Particle.from_pdgid(pdg).mass} AS mass
    FROM Track AS trk
    LEFT JOIN MCParticles AS mcp
      ON mcp.mcparticle_id == trk.mcparticle_id
    LEFT JOIN tmp_closest_to_beam AS ctb
      ON ctb.mcparticle_id == trk.mcparticle_id
    LEFT JOIN tmp_resolution_out AS res
      ON res.mcparticle_id == trk.mcparticle_id
    """ for pdg in (-11, -13, 211, 321, 2212)]


CleanUp = PyLamarr.custom_query([
  "DROP TABLE IF EXISTS tmp_particles_recoed_as",
  "DROP TABLE IF EXISTS tmp_is_muon",
  "DROP TABLE IF EXISTS tmp_closest_to_beam",
  "DROP TABLE IF EXISTS pid",
  "DROP TABLE IF EXISTS ismuoneff",
  "DROP TABLE IF EXISTS covariance",
  ]);

