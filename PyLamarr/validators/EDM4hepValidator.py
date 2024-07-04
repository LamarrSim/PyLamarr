import PyLamarr
import numpy as np
from PyLamarr import RemoteResource
import io
import re
import sys
from dataclasses import dataclass, field
from pydantic import Field, validate_arguments
from typing import Dict, Any, Union

import pandas as pd

DEFAULT_EDM4HEP_YAML = (
  "https://raw.githubusercontent.com/key4hep/EDM4hep/main/edm4hep.yaml"
)


SQLITE_MASTER_QUERY = """
  SELECT name, sql 
  FROM sqlite_master 
  WHERE type=='table'
"""

class EDM4hepValidator:
    def __init__ (self, 
          output_stream: Union[str, io.TextIOWrapper] = sys.stdout,
          edm4hep_yaml: Union[str, RemoteResource] = DEFAULT_EDM4HEP_YAML,
          sql_edm_yaml: Union[str, io.TextIOWrapper] = open('sql_edm.yaml', 'w'),
        ):
        if isinstance(edm4hep_yaml, str):
            edm4hep_yaml = RemoteResource(edm4hep_yaml)

        if isinstance(output_stream, str): 
            output_stream = open(output_stream, "w")

        if isinstance(sql_edm_yaml, str): 
            sql_edm_yaml = open(sql_edm_yaml, "w")

        with open(edm4hep_yaml.file) as input_file:
            loaded_yaml = input_file.read()

        self.config = self.initialize_config(loaded_yaml)
        self.batch_dfs = []
        self.sql_edm_yaml = sql_edm_yaml

    @staticmethod
    def initialize_config(loaded_yaml):
        import yaml
        raw_cfg = yaml.safe_load(loaded_yaml)
        datatypes = raw_cfg['datatypes']

        tables = {}
        for table, desc in datatypes.items():
            this_table, = re.findall(r"edm4hep::([\w0-9_]+).*", table)
            buff = []
            for member_cpp in desc['Members']:
                member_cpp = member_cpp[:member_cpp.find("//")]
                matches = re.findall(
                    r'([\w:0-9]+(?:<[\w,0-9: _]+>)?) *([\w0-9]+)', member_cpp
                    )
                if len(matches) == 0:
                  raise ValueError(f"Could not parse {member_cpp}")
                (dtype, member), *_ = matches
                if re.match("edm4hep::Vector2[df].*", dtype):
                    buff += [('float', f"{member}_x"), ('float', f"{member}_y")]
                elif re.match("edm4hep::Vector3[df].*", dtype):
                    buff += [
                        ('float', f"{member}_x"), 
                        ('float', f"{member}_y"),
                        ('float', f"{member}_z"),
                        ]
                elif re.match("edm4hep::Vector2[i].*", dtype):
                    buff += [('int', f"{member}_x"), ('int', f"{member}_y")]
                elif re.match("edm4hep::Vector3[i].*", dtype):
                    buff += [
                        ('int', f"{member}_x"), 
                        ('int', f"{member}_y"),
                        ('int', f"{member}_z"),
                        ]
                elif re.match("edm4hep::CovMatrix3[df].*", dtype):
                    buff += [
                        ('float', f"{member}_00"), 
                        ('float', f"{member}_01"),
                        ('float', f"{member}_02"),
                        ('float', f"{member}_11"),
                        ('float', f"{member}_12"),
                        ('float', f"{member}_22"),
                        ]
                elif re.match("edm4hep::CovMatrix4[df].*", dtype):
                    buff += [
                        ('float', f"{member}_00"), 
                        ('float', f"{member}_01"),
                        ('float', f"{member}_02"),
                        ('float', f"{member}_03"),
                        ('float', f"{member}_11"),
                        ('float', f"{member}_12"),
                        ('float', f"{member}_13"),
                        ('float', f"{member}_22"),
                        ('float', f"{member}_23"),
                        ('float', f"{member}_33"),
                        ]
                elif re.match("edm4hep::CovMatrix5[df].*", dtype):
                    buff += [
                        ('float', f"{member}_00"), 
                        ('float', f"{member}_01"),
                        ('float', f"{member}_02"),
                        ('float', f"{member}_03"),
                        ('float', f"{member}_04"),
                        ('float', f"{member}_11"),
                        ('float', f"{member}_12"),
                        ('float', f"{member}_13"),
                        ('float', f"{member}_14"),
                        ('float', f"{member}_22"),
                        ('float', f"{member}_23"),
                        ('float', f"{member}_24"),
                        ('float', f"{member}_33"),
                        ('float', f"{member}_34"),
                        ('float', f"{member}_44"),
                        ]
                elif re.match("edm4hep::Quantity", dtype):
                    buff += [
                        ('float', f"{member}_best"), 
                        ('float', f"{member}_err"),
                        ]
                elif re.match("std::array<\w+,[0-9]+>", dtype):
                    (atype, asize), = re.findall("std::array<(\w+), *([0-9]+)>", dtype)
                    asize = int(asize)
                    buff += [ (atype, f"{member}_{i:02d}") for i in range(asize) ]
                elif re.match("std::array<edm4hep::\w+, *[0-9]+>", dtype):
                    (atype, asize), = re.findall("std::array<(edm4hep::\w+), *([0-9]+)>", dtype)
                    asize = int(asize)
                    buff += [ (atype, f"{member}_{i:02d}") for i in range(asize) ]
 
                elif 'edm4hep::' in dtype:
                  raise NotImplementedError(f"Unexpected type {dtype}")
                else:
                    buff.append ((dtype, member))

            if 'OneToOneRelations' in desc:
                for pointer in desc['OneToOneRelations']:
                    pointer = pointer[:pointer.find("//")]
                    (target_table, name), *_ = re.findall(
                        r'edm4hep::([\w0-9_]+) *([\w0-9_]+)', pointer
                        )

                    buff += [('int', name, target_table)]

            if 'OneToManyRelations' in desc:
                for pointer in desc['OneToManyRelations']:
                    pointer = pointer[:pointer.find("//")]
                    (target_table, name), *_ = re.findall(
                        r'edm4hep::([\w0-9_]+) *([\w0-9_]+)', pointer
                        )

                    zip_table = "%s__%s" % tuple(sorted([this_table, target_table]))

                    buff += [('int', name, zip_table)]

            tables[this_table] = [b if len(b)==3 else (*b, None) for b in buff]

        INTEGER_TYPES = ('uint64_t', 'int64_t', 'uint32_t', 'int32_t', 'int')
        REAL_TYPES = ('float', 'double')
        return (
            pd.DataFrame([(k, *v) for k, row in tables.items() for v in row], 
                columns = ["table", "member_type", "member_name", "requires_table"])
            .replace({'member_type': {i: 'INTEGER' for i in INTEGER_TYPES}})
            .replace({'member_type': {i: 'REAL' for i in REAL_TYPES}})
            )
            

    @PyLamarr.method
    def __call__(self, db):
        rows = []
        for name, create in db.execute(SQLITE_MASTER_QUERY).fetchall():
            if "sqlite" in name: continue 

            df = pd.read_sql(f"SELECT * FROM {name} LIMIT 1", db)
            columns = list(df.columns)
            rows += [(name, str(df[c].dtype), c) for c in columns]

        INTEGER_TYPES = ('int64', 'int32')
        REAL_TYPES = ('float64', 'float32')

        self.batch_dfs.append ( 
            pd.DataFrame(rows, columns=['table', 'member_type', 'member_name'])
            .replace({'member_type': {i: 'INTEGER' for i in INTEGER_TYPES}})
            .replace({'member_type': {i: 'REAL' for i in REAL_TYPES}})
            .assign(batch_id=lambda _: len(self.batch_dfs))
            )

    def report_row(self, table, message, column=None):
      if column is None:
          print (f"{table:<33s} | {message:80s}")
      else:
          print (f"{table:<20s} | {column:<10s} | {message:80s}")

    def summary(self):
        df = pd.concat(self.batch_dfs)
        print (df)
        self.batch_dfs = []
        all_batches = np.unique(df.batch_id)
        for expected_table, xpdf in self.config.groupby('table'):
            found = df[df.table == expected_table]
            found_in_batches = np.unique(found.batch_id)
            if len(found) == 0:
                self.report_row(expected_table, "Not found")
                continue 
            else:
                if len(np.setdiff1d(all_batches, found_in_batches)) > 0:
                    self.report_row(expected_table, 
                      f"Found in {len(found_in_batches)}/{len(all_batches)}")
                else:
                    self.report_row(expected_table, "Found")

        try:
            import yaml as output_fmt
        except ImportError:
            import json as output_fmt

        report = {}
        for actual_table, acdf in df.groupby('table'):
            report[actual_table] = np.unique(acdf.member_name).tolist()

        output_fmt.dump(report, self.sql_edm_yaml)


                



#        print (self.config['datatypes'].keys())
#        print (self.config['datatypes']['edm4hep::MCRecoCaloAssociation']['Members'])
#        print (self.config['datatypes']['edm4hep::MCRecoCaloAssociation']['OneToOneRelations'])
#
#        for dtype, desc in self.config['datatypes'].items():
#          if 'OneToManyRelations' in desc:
#            print (dtype, desc['OneToManyRelations'])
#

if __name__ == '__main__':
  validator = EDM4hepValidator()
  from pprint import pprint
  print (validator.config)



