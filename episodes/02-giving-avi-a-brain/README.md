# Building Avi: Giving Avi a Brain

Episode 2 gives Avi a brain, but the brain is not in charge.

Episode 1 gave Avi one safe network tool. Avi could connect to the Cat9k sandbox, run one approved read-only command, summarize the result, and log what happened.

Episode 2 introduces the LLM layer earlier in the journey, but with a strict rule: the LLM can explain evidence, not operate the network.

## Where This Fits in the Avi Journey

Episode 1 gave Avi hands: one safe, approved pyATS tool.

Episode 2 gives Avi a brain, but keeps that brain behind glass.

The LLM does not SSH to devices. It does not choose arbitrary commands. It does not configure anything. It receives a structured report and produces a human-friendly explanation.

Why it matters: the audience gets to meet Avi as an assistant earlier, while the serious NetOps safety story stays intact.

Still out of scope: tool execution by the LLM, autonomous decisions, source of truth comparison, approval workflows, and configuration changes.

## Goal

Take a structured interface report and ask Avi's brain to explain:

- What Avi observed
- What needs review
- What evidence supports the finding
- What safe next step a human should take

## Flight Rules

1. The brain may explain.
2. The brain may summarize.
3. The brain may recommend human review.
4. The brain may not run commands.
5. The brain may not invent network state.
6. The brain may only use the evidence provided.

## Architecture

```text
Network Tool Output -> Structured Evidence -> Avi Brain -> Human Explanation -> Human Review
```

Not this:

```text
User Prompt -> LLM -> Network
```

That distinction is the whole point of this episode.

## What This Episode Adds

- A safe LLM reasoning pattern.
- A prompt template with explicit constraints.
- A deterministic offline brain simulator for the first pass.
- A clear separation between network tools and LLM explanation.

## Run

```bash
cd episodes/02-giving-avi-a-brain
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_02_brain.py
```

## What You Learned

Avi can have a brain without giving that brain control of the network.

The safe pattern is:

```text
Tools collect evidence. The brain explains evidence. Humans review decisions.
```
