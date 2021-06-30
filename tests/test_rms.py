# tests/test_rms.py

import numpy as np

from kallisto.rmsd import rmsd
from tests.store import propanolIntermediate, propanolLowest


def test_rms():
    mol1 = propanolLowest()
    nat1 = mol1.get_number_of_atoms()
    coord1 = mol1.get_positions()
    mol2 = propanolIntermediate()
    coord2 = mol2.get_positions()
    _, u = rmsd(nat1, coord1, coord2)
    if not np.isclose(u[0, 0], 0.98139458):
        raise AssertionError
    if not np.isclose(u[0, 1], -0.04965545):
        raise AssertionError
    if not np.isclose(u[0, 2], -0.18546973):
        raise AssertionError
    if not np.isclose(u[1, 0], 0.06170977):
        raise AssertionError
    if not np.isclose(u[1, 1], 0.9963015):
        raise AssertionError
    if not np.isclose(u[1, 2], 0.05979323):
        raise AssertionError
    if not np.isclose(u[2, 0], 0.18181471):
        raise AssertionError
    if not np.isclose(u[2, 1], -0.07012604):
        raise AssertionError
    if not np.isclose(u[2, 2], 0.98082911):
        raise AssertionError
