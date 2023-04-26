from typing import Tuple, Optional
from dataclasses import dataclass
from pydantic import validate_arguments
from PyLamarr import RemoteResource
from PyLamarr import Wrapper


@validate_arguments
@dataclass(frozen=True)
class CovariancePostprocessing(Wrapper):
    output_table: Optional[str] = "covariance"

    output_columns: Optional[Tuple[str, ...]] = (
        "cov00",
        "cov01", "cov11",
        "cov02", "cov12", "cov22",
        "cov03", "cov13", "cov23", "cov33",
        "cov04", "cov14", "cov24", "cov34", "cov44",
    )

    make_persistent: Optional[bool] = True

    def query(self):
        return """
      WITH shortcut AS (
          SELECT
            sqrt(exp(log_cov_ClosestToBeam_0_0)) AS sig0, 
            sqrt(exp(log_cov_ClosestToBeam_1_1)) AS sig1, 
            sqrt(exp(log_cov_ClosestToBeam_2_2)) AS sig2, 
            sqrt(exp(log_cov_ClosestToBeam_3_3)) AS sig3, 
            sqrt(exp(log_cov_ClosestToBeam_4_4)) AS sig4, 
            corr_ClosestToBeam_0_1               AS cor01,
            corr_ClosestToBeam_0_2               AS cor02,
            corr_ClosestToBeam_1_2               AS cor12,
            corr_ClosestToBeam_0_3               AS cor03,
            corr_ClosestToBeam_1_3               AS cor13,
            corr_ClosestToBeam_2_3               AS cor23,
            corr_ClosestToBeam_0_4               AS cor04,
            corr_ClosestToBeam_1_4               AS cor14,
            corr_ClosestToBeam_2_4               AS cor24,
            corr_ClosestToBeam_3_4               AS cor34
          FROM tmp_covariance_out
        )
      SELECT
        sig0 * sig0,
        cor01 * sig0 * sig1, 
        sig1 * sig1,
        cor02 * sig0 * sig2, 
        cor12 * sig1 * sig2, 
        sig2 * sig2,
        cor03 * sig0 * sig3, 
        cor13 * sig1 * sig3, 
        cor23 * sig2 * sig3, 
        sig3 * sig3,
        cor04 * sig0 * sig4, 
        cor14 * sig1 * sig4, 
        cor24 * sig2 * sig4, 
        cor34 * sig3 * sig4, 
        sig4 * sig4
      FROM shortcut;
      """

    implements: str = "TemporaryTable"

    @property
    def config(self):
        return dict(
            output_table=self.output_table,
            outputs=self.output_columns,
            query=self.query(),
            make_persistent=self.make_persistent,
        )
