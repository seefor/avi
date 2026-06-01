# Episode 03 Walkthrough: Teaching Avi to Read Network State

## 1. Opening Hook

"Avi can now touch the network and record what happened. But raw CLI output is still raw CLI output. Today we teach Avi to turn that output into network state a human can review."

## 2. What We Are Building

```text
Approved Command -> Raw CLI Output -> State Reader -> Interface State Objects -> Human Report
```

Avi is still read-only. The upgrade is interpretation, not autonomy.

## 3. Why State Matters

What to say:

"Operators do not only care that a command ran. They care what the network state means. Up, down, administratively down, unknown. That is where Avi starts becoming more useful."

## 4. Code to Show

- `InterfaceState`
- `classify_interface()`
- `parse_show_ip_interface_brief()`
- `print_state_table()`

## 5. Run the Demo

```bash
python avi_pilot_03_state_reader.py
```

## 6. Teaching Point

Raw output is evidence. Parsed state is interpretation. Avi should keep those ideas separate.

## 7. Homework

1. Add a new `state_label` for `unassigned` IP interfaces.
2. Add a count for interfaces with real IP addresses.
3. Keep all commands read-only.
4. Do not add remediation yet.

## 8. Tease Episode 4

"Next, we make the output more useful for other systems. Humans like tables. Workflows like structured data."
