# Project management demo

This is a demo repo for project management in Technology Workshop 2023.

## Environment management

### Initialize environment

To initialize an environment from scratch:

```sh
mamba create -p ./conda
```

Then install necessary packages in this environment.

### Export environment to file

Exporting environment to `conda.yaml` enables git version tracking and syncing across machines:

```sh
mamba env export -p ./conda --no-build > conda.yaml
```

> **Note**
> We may also chooose to remove the `name:` and `prefix:` lines from the exported file to redact the trace of absolute paths:
> `mamba env export -p ./conda --no-build | grep -Ev '^(name|prefix):' > conda.yaml`

### Clone the environment on another machine

If we wish to use computing resource on another machine, we may clone the repo and rebuild the environment with the `conda.yaml` file.

```sh
mamba env create -p ./conda -f conda.yaml
```

### Sync environment change across machines

If we changed the environment on one machine, we may update the `conda.yaml` file, sync it over git, and use it update the environment on another machine.

```sh
mamba env update -p ./conda -f conda.yaml --prune
```

## Package development

Use the `pyproject.toml` file to instruct the build and install process.

- In this demo, we are using the build tool `flit`.
- Use `flit install -s` to install our own package in symlink mode, so changes in our package are immediately effective without reinstalling.
- To make a formal release of the package, use `flit build` and `twine upload`, or this [github action](https://github.com/pypa/gh-action-pypi-publish).

