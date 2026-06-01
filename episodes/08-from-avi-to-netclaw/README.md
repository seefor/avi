# Building Avi: From Avi to NetClaw

Episode 8 is the capstone for this first Avi arc.

Avi is not NetClaw yet. That is the point. Avi is the careful learning path that teaches the building blocks of a trustworthy network assistant before the system becomes larger, more connected, and more capable.

## Where This Fits in the Avi Journey

Episodes 1 through 7 built the first trust layer for Avi: tool access, evidence, state reading, structured output, multi-device observation, source of truth comparison, and human approval.

Episode 8 connects those pieces into the larger NetClaw direction.

This episode is not about claiming Avi is finished. It is about showing that the small steps were not random. Each one becomes part of a governed assistant skeleton that can grow without skipping safety, observability, or human control.

Why it matters: the path from demo script to useful assistant needs a maturity model, not just more features.

Still out of scope: production deployment, autonomous changes, full orchestration, live NetBox/Tines integrations, and LLM-driven action loops.

## Goal

Map the pieces we built into a larger assistant architecture:

- Tool access
- Black box recording
- State reading
- Structured output
- Multi-device observation
- Source of truth comparison
- Human approval gates
- Future orchestration layer

## Flight Rules

1. Do not confuse a demo script with a production assistant.
2. Keep trust boundaries explicit.
3. Keep tools observable.
4. Keep humans in control of risky decisions.
5. Grow capability only after the foundation is stable.

## Architecture

```text
Avi Building Blocks -> Governed Assistant Skeleton -> NetClaw Direction
```

## What This Episode Adds

- A capability map.
- A maturity view of the assistant.
- A simple architecture model for the next phase.
- A closing story for the first Avi series.

## Run

```bash
cd episodes/08-from-avi-to-netclaw
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_08_capability_map.py
```

## What You Learned

Avi started as one boring tool that worked.

By Episode 8, Avi has the early skeleton of something more serious: a governed, observable, human-reviewed network assistant.
