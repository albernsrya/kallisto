# tests/test_prox.py

import numpy as np

from tests.store import toluene


def test_prox():
    mol = toluene()
    size = (2, 3)
    prox = mol.get_prox(size)
    if not np.isclose(prox[0], 4.381228496800993):
        raise AssertionError
    if not np.isclose(prox[1], 3.3677521592350548):
        raise AssertionError
    if not np.isclose(prox[2], 2.8495247858657446):
        raise AssertionError


def test_prox_different_size():
    mol = toluene()
    size = (1, 2)
    prox = mol.get_prox(size)
    if not np.isclose(prox[0], 5.841080507811956):
        raise AssertionError
    if not np.isclose(prox[1], 5.501735547766682):
        raise AssertionError
    if not np.isclose(prox[2], 5.037814140144763):
        raise AssertionError
