# Episode 02 Walkthrough: The Black Box Recorder

Use this as the camera-ready flow for Episode 2.

## 1. Opening Hook

"In Episode 1, Avi touched the network once and wrote down what happened. That log was simple, but it introduced a serious idea: if automation touches the network, we need evidence. Today we turn that idea into Avi's black box recorder."

Teaching point:

- Trust is not only about the command.
- Trust also comes from the record around the command.

## 2. What We Are Building

```text
User Prompt -> Avi -> Approved Tool -> SSH -> Cat9k Sandbox -> Report -> JSONL Recorder
```

What to say:

"Avi is still not autonomous. It is still not changing anything. We are only making the evidence trail better."

## 3. Recorder Fields

Explain the fields:

- `timestamp`
- `event`
- `tool_name`
- `device_name`
- `command`
- `status`
- `duration_ms`
- `summary`
- `error`

Teaching point:

- If you cannot explain what automation did, you are not ready to let it do more.

## 4. Show the Code

Functions and classes to show:

- `ToolRecord`
- `BlackBoxRecorder`
- `run_recorded_show_command()`
- `print_recent_records()`

Teaching point:

- The recorder is separate from the network tool.
- This makes it reusable later.

## 5. Run the Demo

```bash
python avi_pilot_02_black_box.py
```

What to say:

"The output should look familiar, but now Avi also shows us recent recorder entries. This is the start of auditability."

## 6. Homework

Ask viewers to:

1. Run the script twice.
2. Open `avi_black_box.jsonl`.
3. Compare the timestamps and durations.
4. Try an unapproved command and see how the recorder captures failure.
5. Keep the lab read-only.

## 7. Tease Episode 3

"Now that Avi can record what happened, the next step is teaching it to read network state more carefully. Raw output is useful, but state is what operators care about."
