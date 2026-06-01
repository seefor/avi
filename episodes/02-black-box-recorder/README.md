# Building Avi: The Black Box Recorder

Episode 2 turns Avi's simple JSON Lines log into a reusable flight recorder.

Episode 1 proved Avi could connect to a Cat9k sandbox, run one approved read-only command, summarize the result, and write a log entry. Episode 2 keeps the same safe behavior, but improves the evidence trail around each tool call.

## Where This Fits in the Avi Journey

Episode 1 gave Avi its first safe network instrument: a pyATS SSH tool that could observe one device and report what it saw.

Episode 2 makes the evidence trail more intentional.

Before Avi becomes smarter, it needs a better record of what it did. The Black Box Recorder captures the tool name, device, command, timing, status, summary, and error details when something fails.

Why it matters: trust is not only about getting the right answer. It is also about being able to inspect how Avi got there.

Still out of scope: LLM reasoning, multi-step workflows, source of truth checks, approval workflows, and configuration changes.

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
