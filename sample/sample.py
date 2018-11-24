# coding: utf-8
# Copyright (c) 2018, Taku MURAKAMI. All rights reserved.
# Distributed under the terms of the MIT License.

import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import REA
from REA import RandomExchangeAtoms as Rea

"""
Sample for random-exchange-atoms.py
"""

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    Rea_object = Rea(
        "./sample_input/cif/Al2O3_hR30_R-3c_167.cif",
        format="cif"
    )
    for i in range(3):
        Rea_object.init_struct_dict()
        Rea_object.run_exchange(5)
        Rea_object.modify_cell_size()
        Rea_object.export_dict(filename="./sample_output/POSCAR"+str(i+1))
