# tests/test_lig.py

from kallisto.rmsd import recursiveGetSubstructures
from tests.store import neopentane


def test_lig_neopentane():
    center = 0
    mol = neopentane()
    nat = mol.get_number_of_atoms()
    bonds = mol.get_bonds()
    substructures = recursiveGetSubstructures(nat, bonds, center)  # type: ignore
    if 1 not in substructures[0]:
        raise AssertionError
    if 6 not in substructures[0]:
        raise AssertionError
    if 8 not in substructures[0]:
        raise AssertionError
    if 12 not in substructures[0]:
        raise AssertionError
    center = 1
    substructures = recursiveGetSubstructures(nat, bonds, center)  # type: ignore
    if 6 not in substructures[1]:
        raise AssertionError
    if 8 not in substructures[2]:
        raise AssertionError
    if 12 not in substructures[3]:
        raise AssertionError
