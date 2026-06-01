# Episode 05 Walkthrough: Multi-Device Observation

## 1. Opening Hook

"A single device can teach us the pattern, but real operations rarely stop at one box. Today Avi starts thinking in terms of multiple observations without losing the details from each device."

## 2. What We Are Building

```text
Device Reports -> Per-Device Summaries -> Fleet Summary -> Human Review
```

Avi is still observing only. The new idea is scope.

## 3. Why Multi-Device Observation Matters

What to say:

"If Avi checks one switch, that is useful. If Avi can summarize multiple devices without hiding the individual evidence, it starts looking like the early shape of a real operations assistant."

## 4. Code to Show

- `DeviceObservation`
- `FleetSummary`
- `sample_observations()`
- `build_fleet_summary()`
- `print_device_table()`

## 5. Run the Demo

```bash
python avi_pilot_05_multi_device.py
```

## 6. Teaching Point

Rollups are useful, but they should never erase the details. Avi needs both the fleet view and the device view.

## 7. Homework

1. Add a fourth sample device.
2. Add a `review_priority` field.
3. Sort devices needing review first.
4. Keep this episode observation-only.

## 8. Tease Episode 6

"Next, we introduce a source of truth. Avi has observed the network. Now we ask: does what Avi sees match what we intended?"
