from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments

from PyLamarr import RemoteResource, Wrapper

@validate_arguments
@dataclass(frozen=True)
class RecSummaryEntry:
    name: str
    table_name: str
    count_expr: str = "COUNT (*)"
    selection: Optional[str] = None
    custom_code: Optional[int] = None

    @property
    def code(self):
        if self.custom_code is not None: 
            return self.custom_code 

        codes = dict(
            nPVs = 0, 
            nLongTracks = 10, 
            nDownstreamTracks = 11, 
            nUpstreamTracks = 12,
            nVeloTracks = 13, 
            nTTracks = 14, 
            nBackTracks = 15, 
            nTracks = 16,
            nGhosts = 17, 
            nRich1Hits = 20, 
            nRich2Hits = 21, 
            nVeloClusters = 30,
            nITClusters = 40, 
            nTTClusters = 50, 
            nUTClusters = 51, 
            nOTClusters = 60,
            nFTClusters = 41, 
            nSPDhits = 70, 
            nMuonCoordsS0 = 80,
            nMuonCoordsS1 = 91,
            nMuonCoordsS2 = 92, 
            nMuonCoordsS3 = 93, 
            nMuonCoordsS4 = 94,
            nMuonTracks = 95,
            TypeUnknown = 1000
          )

        if self.name not in codes.keys():
            raise KeyError(
                f"Unknown code for Summary '{self.name}' and no custom_code provided"
            )
              
        return codes[self.name]

    def query(self):
        return f"""
          SELECT 
            e.datasource_id AS event_id,
            {self.code} AS data_key,
            { self.count_expr } AS data_value
          FROM {self.table_name} AS my
          JOIN GenEvents AS e ON my.genevent_id = e.genevent_id
          { 'WHERE ' + self.selection if self.selection is not None else '' }
          GROUP BY e.datasource_id
          """

@validate_arguments
@dataclass(frozen=True)
class RecSummaryMaker(Wrapper):
    output_table: Optional[str] = "RecSummary"
    output_columns: Optional[Tuple[str, ...]] = (
        "event_id", "data_key", "data_value",
      )
    make_persistent: Optional[bool] = True

    def query(self):
        entries = [
              RecSummaryEntry("nPVs", table_name='Vertices'),
              RecSummaryEntry(
                  "nTracks", 
                  table_name='Vertices',
                  count_expr='exp(4.8703 + random_normal()*0.5921)'
              ),
#              RecSummaryEntry(
#                "nTracks", 
#                table_name='GenParticles', 
#                selection=' AND '.join([
#                  'norm2(my.px, my.py, my.pz) > 2500',
#                  'norm2(my.px, my.py, 0) > 150',
#                  'pseudorapidity(my.px, my.py, my.pz) < 5.5',
#                  'pseudorapidity(my.px, my.py, my.pz) > 1.5',
#                  'abs(my.pid) in (11, 13, 211, 321, 2212)',
#                  ]),
#                )
            ]
        
        return [e.query() for e in entries]


    implements: str = "TemporaryTable"

    @property
    def config(self):
        return dict(
            output_table=self.output_table,
            outputs=self.output_columns,
            query=self.query(),
            make_persistent=self.make_persistent,
        )


