# Building Avi: Multi-Device Observation

Episode 5 teaches Avi to think beyond a single device.

So far, Avi has focused on one sandbox device. That is the right way to start. But real network operations rarely stop at one box. In this episode, Avi uses structured sample observations from multiple devices and creates a fleet-level review.

## Goal

Build a simple multi-device observation pattern:

- Read observations from more than one device.
- Summarize each device independently.
- Produce a fleet-level summary.
- Keep individual device evidence visible.
- Avoid making changes.

## Flight Rules

1. Observe only.
2. Keep per-device state separate.
3. Roll summaries up without hiding details.
4. Do not assume one device represents the whole network.
5. Keep the output review-focused.

## Architecture

```text
Device Reports -> Per-Device Summaries -> Fleet Summary -> Human Review
```

## What This Episode Adds

- A multi-device report model.
- Fleet-level counts.
- Per-device health summaries.
- A pattern that can later use live tools safely.

## Run

```bash
cd episodes/05-multi-device-observation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python avi_pilot_05_multi_device.py
```

## What You Learned

Avi should not become a single-device toy. But before it observes multiple real devices, it needs a clean data model for multi-device reporting.
