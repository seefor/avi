# Building Avi: The Black Box Recorder

Episode 3 gives Avi memory of what happened.

Episode 1 gave Avi one safe network tool. Episode 2 gave Avi a brain that can explain evidence without operating the network. Episode 3 now adds a reusable recorder so Avi can keep a clear evidence trail around tool activity and assistant output.

## Where This Fits in the Avi Journey

Episode 2 introduced the brain, but kept that brain behind glass.

Episode 3 gives Avi a better memory.

Before Avi becomes more useful, it needs a better record of what happened. The Black Box Recorder captures the tool name, device, command, timing, status, summary, and error details when something fails.

Why it matters: trust is not only about getting the right answer. It is also about being able to inspect how Avi got there.

Still out of scope: autonomous tool selection, source of truth checks, approval workflows, production orchestration, and configuration changes.

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
cd episodes/03-black-box-recorder
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp testbed.example.yaml testbed.yaml
python avi_pilot_03_black_box.py
```

## What You Learned

Good automation should leave a clear trail. Before Avi becomes more capable, it needs to become easier to audit.
