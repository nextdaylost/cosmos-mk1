from importlib.metadata import version

from cosmos.version import __version__


def test_version():
    assert __version__ == version("cosmos")
