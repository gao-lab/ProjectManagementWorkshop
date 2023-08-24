try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from pkg_resources import get_distribution

    def version(name):
        return get_distribution(name).version


from .model import fit, predict

name = "mypackage"
__version__ = version(name)
