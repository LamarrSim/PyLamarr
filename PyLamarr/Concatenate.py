from typing import Tuple, Optional, Union
from dataclasses import dataclass

from pydantic import validate_arguments, validator

from PyLamarr import RemoteResource, Wrapper


@validate_arguments
@dataclass(frozen=True)
class Concatenate(Wrapper):
    """Concatenate multiple tables. Implements SQLamarr.TemporaryTable."""
    output_table: str
    input_tables: Tuple[str, ...]
    columns: Tuple[str, ...]
    make_persistent: bool = True

    def query(self):
        return list(
            f"SELECT {', '.join(self.columns)} FROM {t}" for t in self.input_tables
        )

    implements: str = "TemporaryTable"

    @property
    def config(self):
        return dict(
            output_table=self.output_table,
            outputs=self.columns,
            query=self.query(),
            make_persistent=self.make_persistent
        )





