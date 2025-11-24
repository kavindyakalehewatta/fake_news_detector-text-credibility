Repository: fake_news_detector-text credibility

**Purpose & Big Picture**:
- **Goal:** small Python project for text-credibility / fake-news detection using CSV datasets in `Data/`.
- **Primary flow:** data lives in `Data/` -> preprocessing utilities in `utils/` -> modelling and training code in `src/` -> CLI/entry in `main.py`.
- **Why this shape:** keeps experiments and model code separate from dataset files; `main.py` is the intended single entrypoint for running pipelines.

**Key Files & Directories**:
- `Data/`: expected CSV datasets (`train.csv`, `test.csv`). Agent should inspect headers and sample rows before assumptions.
- `main.py`: project entrypoint — place orchestration, argument parsing, and high-level pipeline steps here.
- `src/`: implementation modules (data loaders, models, training loops). Prefer `src/data.py`, `src/model.py`, `src/train.py` patterns.
- `utils/`: helper functions (text cleaning, tokenization, metrics). Keep pure helpers here to avoid circular imports.
- `requirement.txt`: dependency list used to install environment (note singular filename here).

**Conventions & Patterns (project-specific)**:
- Single entry CLI: make `main.py` import and call functions from `src/` rather than containing long logic blocks.
- Module layout: prefer small modules with single responsibility, e.g. `src/data.py` exposes `load_train()` and `load_test()`; `src/features.py` exposes `build_features()`.
- Data contract: CSVs expected in `Data/` — always read with explicit encoding and `pd.read_csv(..., dtype=str)` to avoid parsing surprises.
- Dependency file: use `python -m pip install -r requirement.txt` (note the file name).
- Virtualenvs: expect a local venv (not checked into repo). Use `python -m venv .venv` and activate before installing.

**Developer Workflows / Commands**:
- Create + activate venv (PowerShell on Windows):
  - `python -m venv .venv`
  - `.\\.venv\\Scripts\\Activate.ps1`
- Install deps: `python -m pip install -r requirement.txt`
- Run pipeline (when implemented): `python main.py --mode train` (agent should respect common `--mode` or `--config` args if present).

**Integration Points & External Dependencies**:
- Data input: the CSV files under `Data/` are the primary integration point — verify presence and headers.
- No remote services, databases, or CI configuration detected — add network calls or credentials only when documented and secure.

**Code Patterns to Follow / Examples**:
- Prefer small, testable functions. Example expected API:
  - `src/data.py` -> `def load_train(path: str) -> pd.DataFrame`
  - `src/train.py` -> `def train(model, data, config) -> dict`
  - `utils/text.py` -> `def clean_text(s: str) -> str`
- Favor explicit file paths rather than hard-coded globals. Use `Path` from `pathlib`.

**What to look for when editing or adding code**:
- If you add new dependencies, update `requirement.txt`.
- Keep `Data/` read-only in code (avoid writing outputs back into the raw data folder); use `outputs/` or `artifacts/` instead.
- If you add experiments, create a `configs/` directory and document `main.py` arguments to load them.

**When tests or CI are added**:
- Prefer `pytest` and keep tests under `tests/` mirroring `src/` structure.
- Add a `requirements-dev.txt` for test/dev-only tools if needed.

If something in this file seems unclear or you'd like me to expand examples or add recommended starter modules (e.g. `src/data.py` and `src/train.py`), tell me which area to flesh out.
