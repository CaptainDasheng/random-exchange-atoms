# coding: utf-8

from setuptools import setup
from setuptools import find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='random-exchange-atoms',
    version='0.1.0',
    description='Exchange atoms rondomly with pymatgen',
    long_description=readme,
    author='Taku MURAKAMI',
    author_email='murakami.taku.17@shizuoka.ac.jp',
    url='https://github.com/murakami17/random-exchange-atoms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

