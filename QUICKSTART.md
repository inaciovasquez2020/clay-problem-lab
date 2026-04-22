# Clay Problem Lab Quickstart

This is the shortest path from clone to a first successful repository verification pass.

## Requirements

- `git`
- `bash`
- `python3`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/clay-problem-lab.git
cd clay-problem-lab
```

## 2. Check tools

```bash
python3 --version
git --version
```

## 3. Install Python dependencies if needed

```bash
[ -f requirements.txt ] && python3 -m pip install -r requirements.txt || true
```

## 4. Run the pipeline tests

```bash
[ -x scripts/test_pipeline.sh ] && scripts/test_pipeline.sh
python3 -m pytest -q
```

## 5. Review public status surfaces

- `docs/public/START_HERE.md`
- `docs/public/PROOF_STATUS.md`
- `docs/public/INDEPENDENT_VERIFICATION.md`
- `docs/public/WHY_IT_MATTERS.md`

## 6. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
- status surface: `STATUS.md`
