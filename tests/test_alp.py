# tests/test_alp.py

import numpy as np

from tests.store import ch_radical


def test_alp():
    charge = 0
    mol = ch_radical()
    alp = mol.get_alp(charge)
    if not np.isclose(alp[0], 6.56554674):
        raise AssertionError
    if not np.isclose(alp[1], 1.75193793):
        raise AssertionError


def test_alp_cation():
    charge = 1
    mol = ch_radical()
    alp = mol.get_alp(charge)
    if not np.isclose(alp[0], 4.81427623):
        raise AssertionError
    if not np.isclose(alp[1], 1.07449632):
        raise AssertionError


def test_alp_anion():
    charge = -1
    mol = ch_radical()
    alp = mol.get_alp(charge)
    if not np.isclose(alp[0], 9.42323948):
        raise AssertionError
    if not np.isclose(alp[1], 3.25063226):
        raise AssertionError
