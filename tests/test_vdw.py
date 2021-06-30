# tests/test_eeq.py

import numpy as np

from kallisto.units import Bohr
from tests.store import ch_radical


def test_vdw_rahm():
    charge = 0
    vdwtype = "rahm"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 3.29019696):
        raise AssertionError
    if not np.isclose(vdw[1], 2.5041682):
        raise AssertionError


def test_vdw_rahm_angstrom():
    charge = 0
    vdwtype = "rahm"
    scale = Bohr
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 1.74109725):
        raise AssertionError
    if not np.isclose(vdw[1], 1.32514874):
        raise AssertionError


def test_vdw_rahm_cation():
    charge = 1
    vdwtype = "rahm"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 3.14755509):
        raise AssertionError
    if not np.isclose(vdw[1], 2.33524772):
        raise AssertionError


def test_vdw_rahm_anion():
    charge = -1
    vdwtype = "rahm"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 3.46449846):
        raise AssertionError
    if not np.isclose(vdw[1], 2.73535295):
        raise AssertionError


def test_vdw_truhlar():
    charge = 0
    vdwtype = "truhlar"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 2.95785383):
        raise AssertionError
    if not np.isclose(vdw[1], 1.78869157):
        raise AssertionError


def test_vdw_truhlar_angstrom():
    charge = 0
    vdwtype = "truhlar"
    scale = Bohr
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 1.56522884):
        raise AssertionError
    if not np.isclose(vdw[1], 0.94653482):
        raise AssertionError


def test_vdw_truhlar_cation():
    charge = 1
    vdwtype = "truhlar"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 2.82962024):
        raise AssertionError
    if not np.isclose(vdw[1], 1.66803409):
        raise AssertionError


def test_vdw_truhlar_anion():
    charge = -1
    vdwtype = "truhlar"
    scale = 1
    mol = ch_radical()
    vdw = mol.get_vdw(charge, vdwtype, scale)
    if not np.isclose(vdw[0], 3.11454912):
        raise AssertionError
    if not np.isclose(vdw[1], 1.95382353):
        raise AssertionError
