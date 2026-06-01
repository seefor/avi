# Building Avi: Source of Truth

Episode 6 introduces a simple source of truth.

So far, Avi has observed state. That is useful, but observation alone is not enough. Network operators also care about intent: what should exist, what should be reachable, and which interfaces are expected to be active.

## Where This Fits in the Avi Journey

Episode 5 taught Avi how to roll up observations across multiple devices without hiding the per-device details.

Episode 6 introduces intent.

Avi can now ask a better question: does what I observed match what we intended? This is the shift from simple reporting to drift awareness. The source of truth is treated as intent, while observed state is treated as evidence.

Why it matters: a device can be reachable and still be wrong. Avi needs both observed state and intended state before it can provide useful guidance.

Still out of scope: automated corrections, live source of truth APIs, approval workflows, LLM reasoning, and configuration changes.

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
