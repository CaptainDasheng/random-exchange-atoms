# coding: utf-8
# Copyright (c) 2018, Taku MURAKAMI. All rights reserved.
# Distributed under the terms of the MIT License.

import logging
import random
import math
import pymatgen
import pymatgen.io.vasp.inputs as vasp_inputs

from .io.pymatgen_dict import PymatgenDict as PymatDict

"""
Exchange atoms randomly with pymatgen.
"""

logger = logging.getLogger(__name__)


class UndefinedFormatError(Exception):
    """
    Raises exception when user specified undefined format.
    """
    
    def __init__(self, format):
        self.format = format
    
    def __str__(self):
        return("Undefined format '{1}' is specified.".format(self.format))


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
    
    def __init__(self, struct, format="structure",
                 filename="undefined", atom_num_limit=0,
                 output_original_struct_if_modified="True",
                 output_format="poscar", output_path="./"):
        """
        Arguments
        ---------
        struct: (Structure data)
            Original structure data, which can be pymatgen.Structure,
            poscar, cif, or any other what pymatgen can handle.
        format: str
            Format of read data.
        filename: str
            File name of read data.
        atom_num_limit: int
            The lower limit of the number of atoms in the unit cell.
        output_original_struct_if_modified: bool
            If this flag is True, output original structure
            if it is modified in make_supercell_enough_large method.
        output_format: str
            Format of output data of modified original structure.
        output_path: str
            Path to the output file.
        """
        if format is "structure":
            self.struct = struct
        else:
            self.struct = pymatgen.Structure.from_str(
                open(struct).read(),
                fmt=format
            )
        self.filename = filename
        
        struct_if_modified = self.make_supercell_enough_large(atom_num_limit)
        if output_original_struct_if_modified and struct_if_modified:
            if output_format is "poscar":
                with open(output_path + filename + "_modified", mode="w") as file:
                    file.writelines(str(vasp_inputs.Poscar(self.struct)))
            else:
                raise UndefinedFormatError(format)
        
        self.init_struct_dict()
    
    def make_supercell_enough_large(self, atom_num_limit):
        """
        Makes supercell enough large to be our random exchanging effectively.
        
        Arguments
        ---------
        atom_num_limit: int
            The lower limit of the number of atoms in the unit cell.
            If the number is lower than it, make shortest lattice vector
            twice larger by using pymatgen.Structure.make_supercell method.
        """
        original_num_sites = self.struct.num_sites
        while self.struct.num_sites < atom_num_limit:
            lattice_len_dict = dict(zip(
                ["a", "b", "c"], 
                (struct.lattice.a, struct.lattice.b, struct.lattice.c)
            ))
            lattice_smallest_len_key = mix(lattice_len_dict, key=lattice_len_dict.get)
            if lattice_smallest_len_key is "a":
                self.struct.make_supercell([2, 1, 1])
            elif lattice_smallest_len_key is "b":
                self.struct.make_supercell([1, 2, 1])
            else:
                self.struct.make_supercell([1, 1, 2])
        return not original_num_sites == self.struct.num_sites
    
    def init_struct_dict(self):
        """
        Initialize struct_dict with struct.
        """
        self.struct_dict = PymatDict.init_pymatgen_dict(self.struct.as_dict())
        return self
    
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
        return self
    
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
    
    def modify_cell_size(self, probability=10.0, 
                         change_min=-1.0, change_max=1.0):
        """
        Modify cell size randomly.
        
        Arguments
        ---------
        probability: float
            Probability of changing cell size (%).
        change_min: float
            Minimum of changing cell size (% for the length of axes).
        change_max: float
            Maxmum of changing cell size (% for the length of axes).
        """
        len_axis = [] # 0: a-axis, 1: b-axis and 2: c-axis.
        for axis in self.struct_dict["lattice"]["matrix"]:
            len_axis.append(math.sqrt(axis[0]**2+axis[1]**2+axis[2]**2))
        
        for i, axis in enumerate(self.struct_dict["lattice"]["matrix"]):
            for j, element in enumerate(axis):
                if random.uniform(1.0, 100.0) < probability:
                    element += len_axis[i]*random.uniform(
                        change_min/100.0, change_max/100.0
                    )
                    self.struct_dict["lattice"]["matrix"][i][j] = element
                else:
                    pass
        return self
    
    def export_dict(self, format="poscar", filename="./POSCAR"):
        """
        Export edited structure.
        
        Arguments
        ---------
        fortmat: str
            Format of export data (default: "poscar").
        filename: str
            File name (directory) of exported file (default: "./POSCAR").
        """
        struct = pymatgen.Structure.from_dict(self.struct_dict)
        if format is "poscar":
            with open(filename, mode="w") as file:
                file.writelines(str(vasp_inputs.Poscar(struct)))
        else:
            raise UndefinedFormatError(format)
    

if __name__ == "__main__":
    pass
