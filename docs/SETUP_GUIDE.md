# Setup Guide

This guide is for contributors who want a reliable local environment for Clay Problem Lab.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/clay-problem-lab.git
cd clay-problem-lab
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Install dependencies

```bash
[ -f requirements.txt ] && python3 -m pip install -r requirements.txt || true
```

## Verification

```bash
[ -x scripts/test_pipeline.sh ] && scripts/test_pipeline.sh
python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
[ -x scripts/test_pipeline.sh ] && scripts/test_pipeline.sh
python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `STATUS.md`
