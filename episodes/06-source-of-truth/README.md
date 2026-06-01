# Building Avi: Source of Truth

Episode 6 introduces a simple source of truth.

So far, Avi has observed state. That is useful, but observation alone is not enough. Network operators also care about intent: what should exist, what should be reachable, and which interfaces are expected to be active.

## Goal

Compare observed state against intended state:

- Load intended state from YAML.
- Load observed state from sample data.
- Compare interface expectations.
- Report matches, mismatches, and unknowns.
- Keep the result review-focused.

## Flight Rules

1. Read intent before judging state.
2. Treat the source of truth as intent, not reality.
3. Treat observed state as evidence, not intent.
4. Report drift clearly.
5. Do not change the network in this episode.

## Architecture

```text
Source of Truth YAML -> Intent Model
Observed State -> Observation Model
Intent + Observation -> Drift Report -> Human Review
```

## What This Episode Adds

- A simple `source_of_truth.yaml` file.
- Intent models.
- Observation models.
- A drift comparison report.

## Run

```bash
cd episodes/06-source-of-truth
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_06_source_of_truth.py
```

## What You Learned

Avi should not only ask, "What did I see?"

Avi should also ask, "Does what I see match what we intended?"
