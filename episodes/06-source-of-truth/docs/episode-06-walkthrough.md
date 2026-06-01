# Episode 06 Walkthrough: Source of Truth

## 1. Opening Hook

"Avi can observe the network now. But observation is only half the story. Network automation also needs intent. Today we give Avi a simple source of truth and ask whether observed state matches intended state."

## 2. What We Are Building

```text
Source of Truth YAML -> Intent Model
Observed State -> Observation Model
Intent + Observation -> Drift Report -> Human Review
```

## 3. Why Intent Matters

What to say:

"A device can be reachable and still be wrong. An interface can be up and still not match the design. The source of truth gives Avi something to compare against."

## 4. Code to Show

- `source_of_truth.example.yaml`
- `InterfaceIntent`
- `InterfaceObservation`
- `DriftFinding`
- `compare_intent_to_observation()`

## 5. Run the Demo

```bash
python avi_pilot_06_source_of_truth.py
```

## 6. Teaching Point

Intent is not the same thing as reality. Observed state is not the same thing as intent. Avi needs both.

## 7. Homework

1. Add another interface to the source of truth file.
2. Create a matching observation.
3. Create a drift observation.
4. Add a severity field for drift findings.
5. Keep this episode report-only.

## 8. Tease Episode 7

"Now that Avi can detect mismatches, the next dangerous temptation is to let it act. We are not doing that yet. First, we add a human approval gate."
