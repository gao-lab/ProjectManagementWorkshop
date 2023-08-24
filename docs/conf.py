import inspect

import sphinx_autodoc_typehints

import mypackage

project = mypackage.name
version = mypackage.__version__
release = mypackage.__version__
author = "Zhi-Jie Cao"
copyright = "Gao Lab, 2023"

locale_dirs = ["locale"]

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_show_sourcelink = True
set_type_checking_flag = True
typehints_fully_qualified = True
napoleon_use_rtype = False
autosummary_generate = True
autosummary_generate_overwrite = True
autodoc_preserve_defaults = True
autodoc_inherit_docstrings = True
autodoc_default_options = {"autosummary": True}

html_theme = "sphinx_rtd_theme"

intersphinx_mapping = dict(
    python=("https://docs.python.org/3/", None),
    numpy=("https://numpy.org/doc/stable/", None),
    pandas=("https://pandas.pydata.org/pandas-docs/stable/", None),
    sklearn=("https://scikit-learn.org/stable/", None),
)

qualname_overrides = {"pandas.core.frame.DataFrame": "pandas.DataFrame"}

fa_orig = sphinx_autodoc_typehints.format_annotation


def format_annotation(
    annotation, config, fully_qualified=True
):  # pylint: disable=unused-argument
    r"""
    Adapted from https://github.com/agronholm/sphinx-autodoc-typehints/issues/
    38#issuecomment-448517805
    """
    if inspect.isclass(annotation):
        full_name = f"{annotation.__module__}.{annotation.__qualname__}"
        override = qualname_overrides.get(full_name)
        if override is not None:
            return f":py:class:`~{override}`"
    return fa_orig(annotation, config)


sphinx_autodoc_typehints.format_annotation = format_annotation
