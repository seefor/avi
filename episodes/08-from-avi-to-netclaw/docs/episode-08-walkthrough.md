# Episode 08 Walkthrough: From Avi to NetClaw

## 1. Opening Hook

"Avi started with one boring tool that worked. That was intentional. We were not trying to build the full assistant on day one. We were building trust, one capability at a time."

## 2. What We Are Building

```text
Avi Building Blocks -> Governed Assistant Skeleton -> NetClaw Direction
```

This episode is a capstone. It maps the pieces of the first Avi arc into the larger NetClaw direction.

## 3. Capability Map

What to say:

"Each episode gave Avi one new building block. Not a random feature. A trust-building capability."

Capabilities:

1. Tool access
2. Evidence
3. State reading
4. Structured output
5. Multi-device observation
6. Source of truth comparison
7. Human approval
8. NetClaw direction

## 4. Code to Show

- `Capability`
- `build_capability_map()`
- `print_capability_map()`

## 5. Run the Demo

```bash
python avi_pilot_08_capability_map.py
```

## 6. Teaching Point

Avi is not NetClaw yet. Avi is the safe learning path toward NetClaw.

## 7. How to Close the Series

What to say:

"We now have the early skeleton of a real network assistant: it can use tools, record what happened, read state, structure output, compare against intent, and require human approval. That is not flashy, but it is the right foundation."

## 8. Next Arc Ideas

- Add live multi-device collection.
- Add NetBox as a source of truth.
- Add Tines as a workflow layer.
- Add case creation for findings.
- Add controlled approval workflows.
- Add LLM reasoning only after the tool and safety layers are solid.
