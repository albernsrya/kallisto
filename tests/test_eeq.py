# tests/test_eeq.py

import numpy as np

from tests.store import ch_radical


def test_eeq():
    charge = 0
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    if not np.isclose(eeq[0], -0.17166856):
        raise AssertionError
    if not np.isclose(eeq[1], 0.17166856):
        raise AssertionError


def test_eeq_cation():
    charge = 1
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    if not np.isclose(eeq[0], 0.59769359):
        raise AssertionError
    if not np.isclose(eeq[1], 0.40230641):
        raise AssertionError


def test_eeq_anion():
    charge = -1
    mol = ch_radical()
    eeq = mol.get_eeq(charge)
    if not np.isclose(eeq[0], -0.94103071):
        raise AssertionError
    if not np.isclose(eeq[1], -0.05896929):
        raise AssertionError
