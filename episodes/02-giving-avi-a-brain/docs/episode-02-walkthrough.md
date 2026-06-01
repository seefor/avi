# Episode 02 Walkthrough: Giving Avi a Brain

Use this as the camera-ready flow for Episode 2.

## 1. Opening Hook

"In Episode 1, Avi got one safe tool. Today Avi gets a brain, but the brain is not in charge. That is the important part."

## 2. What We Are Building

```text
Network Tool Output -> Structured Evidence -> Avi Brain -> Human Explanation -> Human Review
```

Not this:

```text
User Prompt -> LLM -> Network
```

## 3. Why This Matters

What to say:

"The easy mistake is letting the LLM sit directly in front of the network. We are not doing that. Avi's brain explains evidence. It does not operate tools."

## 4. Flight Rules

1. The brain may explain.
2. The brain may summarize.
3. The brain may suggest human review.
4. The brain may not operate tools.
5. The brain may not invent state.
6. The brain may only use provided evidence.

## 5. Code to Show

- `InterfaceEvidence`
- `EvidenceReport`
- `BrainResponse`
- `BRAIN_RULES`
- `build_prompt()`
- `local_brain()`

## 6. Run the Demo

```bash
python avi_pilot_02_brain.py
```

## 7. Teaching Point

Avi can have a brain without giving that brain control over the network.

The safe pattern is:

```text
Tools collect evidence. The brain explains evidence. Humans review decisions.
```

## 8. Homework

1. Add a new sample interface.
2. Add a `confidence` field to the brain response.
3. Modify the prompt rules to require evidence references.
4. Keep tool operation outside the brain layer.

## 9. Tease Episode 3

"Now Avi has a tool and a brain. Next, we give Avi memory of what happened with a real black box recorder."
