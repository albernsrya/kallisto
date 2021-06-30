# tests/test_strucreader.py

import os

from kallisto.atom import Atom
import kallisto.reader.strucreader as ksr
from kallisto.reader.turbomole import read as tmreader
from kallisto.reader.xyz import read as xyzreader

# define global lineseperator
s = os.linesep


# turbomole coord files can be read
def test_a_user_can_read_coord(fluoromethane_coord):
    fileObject = open(fluoromethane_coord, "r+")
    atoms = ksr.read(fileObject)
    got = type(atoms[0])
    want = Atom
    if got is not want:
        raise AssertionError


def test_user_can_read_xyz(pyridine_xyz):
    fname = open(pyridine_xyz)
    atoms = xyzreader(fname)
    fname.close()
    if len(atoms) != 11:
        raise AssertionError


def test_user_can_read_coord(ch_coord):
    fname = open(ch_coord)
    atoms = tmreader(fname)
    fname.close()
    if len(atoms) != 2:
        raise AssertionError


def test_ignore_coordinates_after_marker(ch_coord_ignore):
    fname = open(ch_coord_ignore)
    atoms = tmreader(fname)
    fname.close()
    if len(atoms) != 2:
        raise AssertionError
    position = atoms[0].get("position")
    if position[0] != 0.0:
        raise AssertionError


def test_user_finds_coordnates_in_coord(ch_coord_2):
    fname = open(ch_coord_2)
    atoms = tmreader(fname)
    fname.close()
    if len(atoms) != 2:
        raise AssertionError
