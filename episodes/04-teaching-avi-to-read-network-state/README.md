# Building Avi: Teaching Avi to Read Network State

Episode 4 teaches Avi to move from evidence explanation toward clearer operational state.

Episode 1 gave Avi a safe tool. Episode 2 gave Avi a brain that explains evidence. Episode 3 gave Avi the recorder concept. Episode 4 teaches Avi to read network state more carefully.

## Where This Fits in the Avi Journey

Episode 3 introduced the memory and evidence layer.

Episode 4 gives Avi a better way to interpret what it sees.

Instead of only showing raw output or a high-level summary, Avi starts turning interface observations into simple state objects. That gives the assistant a cleaner way to explain what it sees while keeping the original observation as evidence.

Why it matters: a network assistant becomes more useful when it can separate observation from interpretation.

Still out of scope: structured JSON contracts, source of truth comparison, approval workflows, production orchestration, and configuration changes.

## Goal

Turn interface observations into a clearer state summary:

- Interface name
- IP address
- Status
- Protocol
- Human-friendly state
- Suggested review note

## Flight Rules

1. Read-only observations only.
2. No configuration mode.
3. No autonomous remediation.
4. Parse state before making claims.
5. When uncertain, say so.

## Architecture

```text
Raw Observation -> State Reader -> Interface State Objects -> Human Report
```

## What This Episode Adds

- A lightweight interface state parser.
- A normalized interface state list.
- A cleaner report that separates raw data from interpretation.
- Simple review notes for down or administratively down interfaces.

## Run

```bash
cd episodes/04-teaching-avi-to-read-network-state
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_04_state_reader.py
```

## What You Learned

Raw output is evidence. Parsed state is how Avi starts becoming useful.

This episode does not make Avi autonomous. It makes Avi easier to trust because the report becomes more structured and more honest.
