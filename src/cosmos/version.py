"""Package version metadata.

Exposes package version in a single canonical location, avoiding issues with
circular import which arise from defining __version__ directory in the package
__init__.py.
"""


from importlib.metadata import version


__version__ = version("cosmos")
