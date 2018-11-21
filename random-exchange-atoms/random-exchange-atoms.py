# coding: utf-8

import logging
import random
import pymatgen

from .io.pymatgen_dict import PymatgenDict as PymatDict

"""
Exchange atoms randomly with pymatgen.
"""

logger = logging.getLogger(__name__)


class RandomExchangeAtoms(object):
    """
    Exchange atoms randomly with pymatgen.
    
    Parameters
    ----------
    struct: pymatgen.Structure object
        Original structure data.
    struct_dict: dict
        Structure data which can be exchange atom positions.
    """
    
    def __init__(self, struct, format="structure"):
        """
        Arguments
        ---------
        struct: (Structure data)
            Original structure data, which can be pymatgen.Structure,
            poscar, cif, or any other what pymatgen can handle.
        format: str
            Format of read data.
        """
        if format is "structure":
            self.struct = struct
        else:
            self.struct = pymatgen.Structure.from_str(
                open(struct).read(),
                fmt=format
            )
        
        self.struct_dict = PymatDict.init_pymatgen_dict(
            self.struct.as_dict()
        )
    
    def run_exchange(self, number=100):
        """
        Run random exchange of atoms in structure.
        
        Arguments
        ---------
        number: int
            Number of exchange atoms (default: 100).
        """
        for i in range(number):
            atom1 = random.randint(0, len(self.struct_dict["sites"])-1)
            atom2 = random.randint(0, len(self.struct_dict["sites"])-1)
            self._swap_atom(atom1, atom2)
        self._sort_atom()
    
    def _swap_atom(self, atom1, atom2):
        """
        Swap two atoms in struct_dict.
        
        Arguments
        ---------
        atom1, atom2: int
            Index of two swapping atoms in struct_dict.
        """
        element1 = self.struct_dict["sites"][atom1]["species"][0]["element"]
        element2 = self.struct_dict["sites"][atom2]["species"][0]["element"]
        self.struct_dict["sites"][atom1]["species"][0]["element"] = element2
        self.struct_dict["sites"][atom2]["species"][0]["element"] = element1
    
    def _sort_atom(self):
        """
        Sort atoms in struct_dict with key of atomic species.
        """
        sites_dict = self.struct_dict["sites"]
        sites_dict = sorted(
            sites_dict, key=lambda x:x["species"][0]["element"]
        )
        self.struct_dict["sites"] = sites_dict
    
    def export_dict(self, format="poscar"):
        """
        Export edited structure.
        
        Arguments
        ---------
        fortmat: str
            Format of export data (default: "poscar").
        """
        pass
    

if __name__ == "__main__":
    pass
