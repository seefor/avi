# Building Avi: The Black Box Recorder

Episode 2 turns Avi's simple JSON Lines log into a reusable flight recorder.

Episode 1 proved Avi could connect to a Cat9k sandbox, run one approved read-only command, summarize the result, and write a log entry. Episode 2 keeps the same safe behavior, but improves the evidence trail around each tool call.

## Goal

Build a small reusable recorder that captures:

- Tool name
- Device name
- Command
- Start time
- End time
- Duration
- Status
- Summary
- Error details when something fails

## Flight Rules

1. Read-only commands only.
2. No configuration mode.
3. No autonomous decisions.
4. Every tool call is recorded.
5. A human can inspect the evidence after the run.

## Architecture

```text
User Prompt -> Avi -> Approved Tool -> SSH -> Cat9k Sandbox -> Report -> JSONL Recorder
```

## What This Episode Adds

- A reusable `BlackBoxRecorder` helper.
- Start and finish records.
- Duration tracking.
- Success and failure details.
- A simple reader for recent log entries.

## Run

```bash
cd episodes/02-black-box-recorder
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp testbed.example.yaml testbed.yaml
python avi_pilot_02_black_box.py
```

## What You Learned

Good automation should leave a clear trail. Before Avi becomes smarter, it needs to become easier to audit.
