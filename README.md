# ci-github-actions-demo

This repository is used for practicing Continuous Integration (CI) with **GitHub Actions**.

## What’s inside
- Basic CI workflow on push to `main`
- Python tests with `unittest`
- Scheduled workflow via `cron`
- Matrix builds for Python versions

## 📦 Repository Structure
```
.
├── main.py
├── test_main.py
├── requirements.txt
└── .github/
└── workflows/
├── ci-basic.yml # Task 1: echo on push to main
├── ci-tests.yml # Task 2 + Task 4: tests (matrix builds)
└── ci-schedule.yml # Task 3: daily scheduled job (midnight UTC)
```

---

## 🧪 Tasks Overview

### ✅ Task 1 — Basic Workflow on Push
**Goal:** When code is pushed to `main`, a job runs and prints a message.  
**File:** `.github/workflows/ci-basic.yml`  
**Key points:**
- `on: push` to `main`
- `actions/checkout@v3`
- `run: echo "Hello, CI with GitHub Actions!"`

**Why:** Proves Actions is wired up and can execute a job.

---

### ✅ Task 2 — Run Unit Tests (Python 3.9)
**Goal:** Add Python code + tests and run them in CI on each push/PR.  
**Files:** `main.py`, `test_main.py`, `.github/workflows/ci-tests.yml`  
**Workflow highlights:**
- `actions/setup-python@v4` with `python-version: "3.9"`
- `pip install -r requirements.txt` (safe even if empty)
- `python -m unittest discover -v`

**Why:** Validates code with automated tests in CI.

---

### ✅ Task 3 — Cron Scheduling (Midnight UTC)
**Goal:** Run a workflow **daily at 00:00 UTC** and log a message.  
**File:** `.github/workflows/ci-schedule.yml`  
**Workflow highlights:**
- `on.schedule: - cron: "0 0 * * *"`
- Includes `workflow_dispatch` (manual run) for instant testing
- Prints: `Scheduled build completed successfully!`

**Why:** Demonstrates scheduled CI executions.

---

### ✅ Task 4 — Matrix Builds (3.7, 3.8, 3.9, 3.10)
**Goal:** Run the same tests across multiple Python versions.  
**File:** `.github/workflows/ci-tests.yml`  
**Matrix detail:**
- Default entries: `3.8`, `3.9`, `3.10` on `ubuntu-latest` (24.04)
- Special case: `3.7` on `ubuntu-22.04` (because 3.7 isn’t available on 24.04)

```yaml
strategy:
  fail-fast: false
  matrix:
    python-version: ["3.8", "3.9", "3.10"]
    os: [ubuntu-latest]
    include:
      - python-version: "3.7"
        os: ubuntu-22.04

```

**Why:** Ensures compatibility across multiple runtimes (common CI requirement).

### ▶️ How to Trigger the Workflows

- **Task 1:**  (ci-basic.yml): push a commit to main.

- **Task 2/4:**  (ci-tests.yml): push to main or open a PR targeting main.

- **Task 3:**  (ci-schedule.yml):

    - Automatic - runs every day at 00:00 UTC.

    - Manual- Actions tab → CI - Daily Scheduled Job → Run workflow.

**Where to see logs:** Repo → Actions → select a run → open job steps.

### 📝 Code Under Test

- `main.py` - exposes add(a, b).

- `test_main.py` - (unittest) checks positive/zero/negative cases.

- Tests are discovered via python -m unittest discover -v.


### 🧰 Notes & Good Practices

- Keep secrets out of the repo and workflows.

- Keep dependencies in requirements.txt (even if empty today).

- Use small commits to make pipeline debugging easy.

### ⭐ Bonus (Optional): Self-Hosted Runner

If you want extra credit, you can run a job on your own machine (e.g., WSL).
High-level steps:

1. Repo → Settings → Actions → Runners → New self-hosted runner (choose Linux).

2. GitHub shows exact commands to:

    - Download the runner package

    - Configure it (uses a registration token)

    - Start it (foreground or as a service)

Example workflow job section to target your runner:

```yaml
jobs:
  on-self-hosted:
    name: Run on my self-hosted runner
    runs-on: [self-hosted, linux, x64]
    steps:
      - uses: actions/checkout@v3
      - run: echo "Hello from my self-hosted runner!"

```
Remember to start the runner before triggering the workflow. Stop it after you’re done.

