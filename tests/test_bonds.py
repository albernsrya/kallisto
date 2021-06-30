# tests/test_bonds.py

from tests.store import ch_radical, pyridine, toluene


def test_bonds_ch_radical():
    mol = ch_radical()
    bonds = mol.get_bonds()
    if bonds[0] != [1]:
        raise AssertionError
    if bonds[1] != [0]:
        raise AssertionError


def test_bonds_pyridine():
    mol = pyridine()
    bonds = mol.get_bonds()
    if bonds[0] != [1, 5, 6]:
        raise AssertionError
    if bonds[1] != [0, 2, 7]:
        raise AssertionError
    if bonds[4] != [3, 5, 10]:
        raise AssertionError


def test_bonds_toluene_partner():
    mol = toluene()
    partner = 1
    bonds = mol.get_bonds(partner)
    if bonds != [0, 2, 8]:
        raise AssertionError
    partner = 5
    bonds = mol.get_bonds(partner)
    if bonds != [0, 4, 6]:
        raise AssertionError
