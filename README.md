# random-exchange-atoms; REA

![Python-version](https://img.shields.io/badge/Python-3.6-green.svg)
![MIT-LICENSE](https://img.shields.io/badge/licence-MIT-blue.svg)

In this package, you can exchange atoms in crystal structures randomly with pymatgen. 

## Requirement

### Python

In this package you should use [python](https://www.python.org/) 3.5 or later.

### Pymatgen

We use [pymatgen](https://github.com/materialsproject/pymatgen)
in order to handle crystal structures on your computer.

If you have pip, you can install pymatgen as follows:

~~~~
> pip install --user pymatgen
~~~~

## Usage

First, you must read structure file from "cif", "poscar", "pymatgen.Structure"
or many other structural format which can be handle in pymatgen package as follows:

~~~~
> from REA import RandomExchangeAtoms as rea

> rea_object = rea("./sample_input/cif/Al2O3_hR30_R-3c_167.cif", format="cif")
~~~~

If you want to exchange atoms randomly, you can use **run_exchange(number)** method
where **number** is integer which means number of exchange.

~~~~
rea_object.run_exchange(5)
~~~~

If you also think to change cell shape, you can use **modify_cell_size()** method.

~~~~
rea_object.modify_cell_size()
~~~~

In order to export your newly structure,
you should call **export_dict(filename)** method.

~~~~
rea_object.export_dict(filename="new_structure")
~~~~

In the default setting export data is the POSCAR (VASP) format.

## Install

Clone this package.

## Licence

~~~~
MIT License

Copyright (c) 2018 Taku MURAKAMI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
~~~~

## Author

Taku MURAKAMI[@murakami17](https://github.com/murakami17/),
master course student at Shizuoka university.

Please contant me via:
[e-mail](mailto:murakami.taku.17@shizuoka.ac.jp) or
[github issues](https://github.com/murakami17/cif2fp/issues).
