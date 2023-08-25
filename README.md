# Project management demo

[![stars-badge](https://img.shields.io/github/stars/gao-lab/ProjectManagementWorkshop?logo=GitHub&color=yellow)](https://github.com/gao-lab/ProjectManagementWorkshop/stargazers)
[![build-badge](https://github.com/gao-lab/ProjectManagementWorkshop/actions/workflows/test.yaml/badge.svg)](https://github.com/gao-lab/ProjectManagementWorkshop/actions/workflows/test.yaml)
[![license-badge](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a demo repo for project management in Technology Workshop 2023.

## Environment management

### Initialize environment

To initialize an environment from scratch:

```sh
mamba create -p ./conda
```

Then install necessary packages in this environment.

### Export environment to file

Exporting environment to `conda.yaml` enables git version tracking and syncing
across machines:

```sh
mamba env export -p ./conda --no-build > conda.yaml
```

> **Note**
>
> We may also choose to remove the `name:` and `prefix:` lines from the exported
> file to redact the trace of absolute paths, as well as to remove our
> "mypackage" entry which should be installed as a development version. Here
> I've also ignored os-specific entries to support multiple os, but that's
> unnecessary if you only aim for a single os like linux:
>
> ```sh
> mamba env export -p ./conda --no-build | grep -Ev '^name|^prefix|mypackage' |
> grep -Ev 'linux|lib|keyutils|openmp|sed|osx|pyobjc|clang|llvm|compiler-rt' >
> conda.yaml
> ```

### Clone the environment on another machine

If we wish to use computing resource on another machine, we may clone the repo
and rebuild the environment with the `conda.yaml` file.

```sh
mamba env create -p ./conda -f conda.yaml
```

### Sync environment change across machines

If we changed the environment on one machine, we may update the `conda.yaml`
file, sync it over git, and use it update the environment on another machine.

```sh
mamba env update -p ./conda -f conda.yaml --prune
```

## Package development

Use the `pyproject.toml` file to instruct the build and install process.

- In this demo, we are using the build tool `flit`.
- Use `flit install -s` to install our own package in symlink mode, so changes
  in our package are immediately effective without reinstalling.
- To make a formal release of the package, use `flit build` and `twine upload`,
  or this [github action](https://github.com/pypa/gh-action-pypi-publish).


## Run unit tests

```sh
pytest --cov
```

## Build documentation

```sh
sphinx-build -b html docs docs/_build
```

## Data preparation

Go to the `data/download` directory, download each dataset as described in their
README file, and run the preprocessing scripts. These will produce a
`data/processed` directory containing standardized data files.

## Run evaluation

Go to the `evaluation` directory, and run the following command:

```sh
snakemake -prk -j4
```

## Run experiments

Go to the `experiments` subdirectories, and convert percent scripts to Jupyter
notebooks with the following command:

```sh
jupytext --to notebook *.py
```

Then play with the notebooks in Jupyter Lab. They will stay in sync with the
percent script automatically.
