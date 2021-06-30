# tests/test_stm.py

import numpy as np

from kallisto.sterics import getClassicalSterimol
from tests.store import toluene


def test_stm():
    mol = toluene()
    origin = 6
    partner = 5
    L, bmin, bmax = getClassicalSterimol(mol, origin, partner)
    if not np.isclose(L, 12.714385):
        raise AssertionError
    if not np.isclose(bmin, 3.539068):
        raise AssertionError
    if not np.isclose(bmax, 6.640342):
        raise AssertionError
