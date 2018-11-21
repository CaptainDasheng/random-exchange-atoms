# coding: utf-8

import logging
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)
import REA
from REA.main import RandomExchangeAtoms as REA

"""
Sample for random-exchange-atoms.py
"""

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    REA_object = REA(
        "./sample_input/cif/Al2O3_hR30_R-3c_167.cif",
        format="cif"
    )
    for i in range(3):
        REA_object.init_struct_dict()
        REA_object.run_exchange(5)
        REA_object.modify_cell_size()
        REA_object.export_dict(filename="./sample_output/POSCAR"+str(i+1))
