# TDD-with-python-code

![ci](https://github.com/5ara5t1/TDD-with-python-code/actions/workflows/tests.yml/badge.svg)

A Django to-do list app built test-first while working through [Test-Driven Development with Python](https://www.obeythetestinggoat.com/) (3rd edition) by Harry Percival.

I typed every line by hand and reviewed each chapter the next day. The app design and most of the code follow the book. The CI pipeline and project tooling are my own additions; I used an LLM and web searches to debug the pipeline and answer GitHub Actions questions.

## What's here

- `src/`: the Django project (`superlists`) and its `lists` app
- `tests/unit/`: unit tests, run with pytest
- `tests/functional/`: browser tests with Selenium and Firefox
- `.github/workflows/tests.yml`: the CI pipeline

Each chapter is developed on its own branch (`ch03`, `ch04`, ...) and merged into `main`.

## CI

Every push and pull request runs three jobs in order, each gating the next:

1. Lint with ruff
2. Unit tests
3. Functional tests in headless Firefox, with one retry and artifacts uploaded on failure

## Run it

Requires [uv](https://docs.astral.sh/uv/). The functional tests also need Firefox and geckodriver.

```bash
uv sync
uv run pytest tests/unit -v
uv run pytest tests/functional -v
```
