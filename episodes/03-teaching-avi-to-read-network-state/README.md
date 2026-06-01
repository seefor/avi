# Building Avi: Teaching Avi to Read Network State

Episode 3 teaches Avi to move from raw CLI output toward a clearer operational state summary.

Avi still uses approved read-only commands. It still does not configure anything. The improvement in this episode is interpretation: Avi starts turning interface output into simple state objects a human can review.

## Where This Fits in the Avi Journey

Episode 2 gave Avi a better evidence trail with the Black Box Recorder.

Episode 3 teaches Avi to read network state more carefully.

Instead of only counting interfaces or printing raw command output, Avi starts turning CLI text into simple state objects. That gives the assistant a cleaner way to explain what it sees while keeping the raw command as the original evidence.

Why it matters: a network assistant becomes more useful when it can separate observation from interpretation.

Still out of scope: structured JSON contracts, multi-device rollups, source of truth comparison, approval workflows, and configuration changes.

## Goal

Turn `show ip interface brief` output into a clearer state summary:

- Interface name
- IP address
- Status
- Protocol
- Human-friendly state
- Suggested review note

## Flight Rules

1. Read-only commands only.
2. No configuration mode.
3. No autonomous remediation.
4. Parse state before making claims.
5. When uncertain, say so.

## Architecture

```text
Approved Command -> Raw CLI Output -> State Reader -> Interface State Objects -> Human Report
```

## What This Episode Adds

- A lightweight interface state parser.
- A normalized interface state list.
- A cleaner report that separates raw data from interpretation.
- Simple review notes for down or administratively down interfaces.

## Run

```bash
cd episodes/03-teaching-avi-to-read-network-state
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp testbed.example.yaml testbed.yaml
python avi_pilot_03_state_reader.py
```

## What You Learned

Raw output is evidence. Parsed state is how Avi starts becoming useful.

This episode does not make Avi autonomous. It makes Avi easier to trust because the report becomes more structured and more honest.
