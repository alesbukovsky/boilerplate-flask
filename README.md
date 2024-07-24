# Flask Boilerplate

A simple API prototyping boilerplate with [Flask](https://flask.palletsprojects.com/), including unit testing ([pytest](https://docs.pytest.org)) and linting ([ruff](https://docs.astral.sh/ruff/)).

## Prerequisites

- Python 3.12+

## Usage

Create and activate a Python virtual environment.

```shell
python -m venv .venv
source .venv/bin/activate
```

Install dependencies, including those for development. Note that the `\` are only needed for `zsh` to bypass pattern matching.

```shell
pip install -e .\[dev\]
```

Check available development commands and run any.

```shell
dev -h
dev <command>
```