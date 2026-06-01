# Episode 04 Walkthrough: Structured Output and Parsing

## 1. Opening Hook

"Humans like readable reports. Workflows like predictable data. In this episode, Avi starts producing structured output that another system could safely consume."

## 2. What We Are Building

```text
Parsed State -> Validated Model -> JSON Report -> Human Review
```

Avi is still review-only. The improvement is structure.

## 3. Why Structured Output Matters

What to say:

"If Avi only prints nice text, it is useful for a person watching the terminal. If Avi produces validated JSON, it becomes useful to a workflow, a dashboard, a case system, or a future assistant."

## 4. Code to Show

- `InterfaceRecord`
- `InterfaceSummary`
- `AviInterfaceReport`
- `build_summary()`
- `save_report()`

## 5. Run the Demo

```bash
python avi_pilot_04_structured_output.py
```

## 6. Teaching Point

Structured output is a contract. If another system depends on Avi, Avi needs predictable data.

## 7. Homework

1. Add a new field called `review_severity`.
2. Add a schema version note to the README.
3. Open the generated JSON file.
4. Keep this episode focused on reporting.

## 8. Tease Episode 5

"Now that Avi can produce structured state, we can ask a bigger question: what happens when Avi observes more than one device?"
