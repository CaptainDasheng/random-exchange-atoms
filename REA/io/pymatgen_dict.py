# coding: utf-8
# Copyright (c) 2018, Taku MURAKAMI. All rights reserved.
# Distributed under the terms of the MIT License.

import pymatgen

"""
Initialize dict of pymatgen.Structure
"""


class PymatgenDict(object):
    """
    Initialize dict of pymatgen.Structure.
    """
    
    @classmethod
    def init_pymatgen_dict(cls, dict):
        """
        Initialize dict of pymetgen.Structure.
        
        In this classmethod, we set None to
        a, b, c, alpha, beta, gamma and volume of pymatgen_dict["lattice"]
        and xyz of all elements of pymatgen_dict["sites"].
        
        Arguments
        ---------
        dict: pymatgen.Structure.as_dict()
            dict of pymatgen.Structure
        
        Returns
        -------
        dict: pymatgen.Structure.as_dict()
            Edited dict of pymatgen.Structure
        
        !!!Cautions!!!
            In this method we do not check given dict is generated from
            pymatgen.Structure.as_dict().
        """
        for key in dict["lattice"].keys():
            if key is "matrix":
                pass
            else:
                dict["lattice"][key] = None
        
        for site in dict["sites"]:
            site["xyz"] = None
        
        return dict

if __name__ == "__main__":
    pass
