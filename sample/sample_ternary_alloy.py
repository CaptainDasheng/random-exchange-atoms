# coding: utf-8
# Copyright (c) 2018, Taku MURAKAMI. All rights reserved.
# Distributed under the terms of the MIT License.

import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pymatgen
import REA
from REA import RandomExchangeAtoms as Rea

"""
Sample for random-exchange-atoms.py to generate models of ternary_alloys.
"""

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    structs_name_tuple = ("Fe4OF7", "Fe4OF8", "Fe6OF11",)
    structs_dict = {}
    for struct_name in structs_name_tuple:
        structs_dict[struct_name] = pymatgen.Structure.from_str(
            open("./sample_input/ternary_alloys/POSCAR_" + struct_name).read(),
            fmt="poscar"
        )
    
    for struct_name, struct in structs_dict.items():
        obj = Rea(
            struct,
            filename=struct_name,
            atom_num_limit=20,
            output_format="poscar",
            output_path="./sample_output/sample_ternary_alloy/" + struct_name + "/"
        )
        for i in range(33):
            obj.run_exchange(5)
            obj.modify_cell_size(probability=20.0)
            obj.export_dict(
                filename="./sample_output/sample_ternary_alloy/" + \
                         struct_name + "/POSCAR"+ str(i+1)
            )
