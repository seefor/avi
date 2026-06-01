# Building Avi: Structured Output and Parsing

Episode 4 turns Avi's interface state into structured data that other tools can read.

In Episode 3, Avi created readable interface state objects. In this episode, we make the output stricter and more portable by producing validated JSON.

## Where This Fits in the Avi Journey

Episode 3 taught Avi to turn raw interface output into simple state objects.

Episode 4 turns those state objects into validated structured output.

This is the point where Avi starts producing data that is useful beyond the terminal. A human can still read the report, but another workflow, dashboard, or future assistant can also consume the same JSON safely.

Why it matters: structured output becomes the contract between Avi and the systems that may use Avi's findings later.

Still out of scope: live multi-device collection, source of truth comparison, approval decisions, LLM reasoning, and configuration changes.

## Goal

Create a structured report with:

- Device name
- Command used
- Interface records
- Summary counts
- Review notes
- Schema version

## Flight Rules

1. Keep the lab read-only.
2. Keep raw observations separate from interpretation.
3. Validate output before trusting it.
4. Prefer structured JSON for workflow handoff.
5. Keep this episode focused on review and reporting.

## Architecture

```text
Parsed State -> Validated Model -> JSON Report -> Human Review
```

## What This Episode Adds

- Pydantic models for interface state.
- A schema version for the report.
- JSON output that can be saved and reused.
- A clean boundary between display output and machine output.

## Run

```bash
cd episodes/04-structured-output-and-parsing
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_04_structured_output.py
```

## What You Learned

Text is good for people. Structured output is better for systems.

This episode prepares Avi for later integrations while keeping the assistant review-only.
