# Episode 07 Walkthrough: Human-in-the-Loop Safety

## 1. Opening Hook

"Avi can now find things worth reviewing. That does not mean Avi should act on them. Today we add the safety gate: a human decision before anything moves forward."

## 2. What We Are Building

```text
Finding -> Recommendation -> Approval Packet -> Human Decision -> Saved Review Record
```

## 3. Why Human Approval Matters

What to say:

"The dangerous leap is going from observation to action too quickly. In real operations, approval is not just a checkbox. It is where context, risk, timing, and ownership come together."

## 4. Code to Show

- `RecommendationPacket`
- `ApprovalRecord`
- `ask_for_decision()`
- `execution_allowed=False`

## 5. Run the Demo

```bash
python avi_pilot_07_human_gate.py
```

Choose one of:

- `approve`
- `reject`
- `defer`

## 6. Teaching Point

Approval is control. Rejection and deferral are valid outcomes.

## 7. Homework

1. Add a `reviewer_name` field.
2. Add a `risk_level` field.
3. Save multiple approval records as JSON Lines.
4. Keep execution disabled.

## 8. Tease Episode 8

"Now we have the skeleton: observe, log, structure, compare, and review. Next, we talk about how Avi becomes the early path toward NetClaw."
