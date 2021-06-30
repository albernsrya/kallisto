# test/test_atom.py

from kallisto.atom import Atom
from kallisto.molecule import Molecule


def test_user_can_create_an_atom():
    symbol = "C"
    atomPosition = [0, 0, 0]
    atom = Atom(symbol=symbol, position=atomPosition)
    if atom.symbol != "C":
        raise AssertionError


def test_user_can_set_an_atom_symbol():
    symbol = "C"
    atomPosition = [0, 0, 0]
    atom = Atom(symbol=symbol, position=atomPosition)
    atom.set("symbol", "N")
    if atom.symbol != "N":
        raise AssertionError


def test_user_can_get_an_atom_symbol():
    atom = Atom(symbol="C", position=[0, 0, 0])
    got = atom.get("symbol")
    want = "C"
    if got != want:
        raise AssertionError


def test_user_can_create_atom_from_element_string():
    atom = Atom("H")
    if atom.symbol != "H":
        raise AssertionError


def test_user_can_modify_atom_via_element_number():
    atom = Atom("H")
    atom.number = 6
    if atom.symbol != "C":
        raise AssertionError


def test_molecule_is_not_none():
    atoms = []
    for i in range(2):
        atoms.append(Atom(symbol="H", position=(0, 0, i)))
    molecule = Molecule(atoms)
    atom = Atom(symbol="H", position=(0, 0, 4), molecule=molecule)
    if atom.molecule is None:
        raise AssertionError
