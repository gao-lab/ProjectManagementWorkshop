try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from pkg_resources import get_distribution

    def version(name):
        return get_distribution(name).version


name = "mypackage"
version = version(name)

from .model import fit, predict
