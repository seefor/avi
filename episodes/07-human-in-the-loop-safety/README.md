# Building Avi: Human-in-the-Loop Safety

Episode 7 adds an approval gate.

Avi can now observe state, structure output, review multiple devices, and compare observed state against intended state. That does not mean Avi should act on its own. This episode introduces a simple approval workflow that separates recommendations from execution.

## Where This Fits in the Avi Journey

Episode 6 taught Avi to compare observed state against intended state and identify drift for review.

Episode 7 adds the control layer.

This is where Avi learns that a finding is not the same thing as permission to act. The assistant can package a recommendation, explain the risk, and ask for a human decision. Approval, rejection, and deferral are all valid outcomes.

Why it matters: safe network assistants need clear boundaries between suggestion, approval, and execution.

Still out of scope: executing changes, automatic remediation, live ticket creation, LLM reasoning, and production workflow orchestration.

## Goal

Build a review packet that a human can approve, reject, or defer:

- Finding summary
- Suggested next step
- Risk note
- Required approval status
- Final decision

## Flight Rules

1. Avi may recommend.
2. Avi may not execute changes.
3. A human must approve before any action is considered.
4. Rejections and deferrals are valid outcomes.
5. The approval record must be saved.

## Architecture

```text
Finding -> Recommendation -> Approval Packet -> Human Decision -> Saved Review Record
```

## What This Episode Adds

- A recommendation object.
- A human approval prompt.
- An approval record saved as JSON.
- A clean separation between "suggest" and "do".

## Run

```bash
cd episodes/07-human-in-the-loop-safety
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_07_human_gate.py
```

## What You Learned

A safe assistant should not turn every finding into an action.

The human approval gate is not friction. It is control.
