# tests/test_version.py

from kallisto import __version__


def test_version():
    if __version__ != "1.0.7":
        raise AssertionError
