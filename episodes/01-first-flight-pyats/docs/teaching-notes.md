# Teaching Notes

These notes support Episode 1 and help explain the ideas behind the code.

## pyATS Testbed

A pyATS testbed is a YAML file that describes the network lab. It tells pyATS which devices exist, what operating system they run, how to connect, and which credentials to use.

For Avi, the testbed is the starting map. Instead of hardcoding device details directly in Python, we keep them in `testbed.yaml`.

This is useful because:

- The code can stay focused on behavior.
- The lab inventory can change without rewriting the script.
- Real credentials can stay out of Git.

## Unicon Connection

Unicon is the connection layer used by pyATS for CLI devices. In Episode 1, Avi asks pyATS to connect to `core-r1` using the `cli` connection from the testbed. Unicon handles the SSH session, device prompt, login flow, enable mode, and command execution behavior.

The important beginner takeaway:

pyATS loads the device model. Unicon handles the live CLI connection.

## Why Read-Only Comes First

Read-only automation is the safest first step because it observes without changing the network.

Before Avi can make recommendations, open tickets, build change plans, or eventually help with remediation, it needs to prove that it can collect facts reliably.

Episode 1 only runs:

```text
show ip interface brief
```

No configuration mode. No changes. No shortcuts.

## Why Tools Matter

An agent without tools can talk about a network, but it cannot inspect the real network.

Tools are how Avi reaches outside the prompt and gathers evidence. In Episode 1, the tool is a simple Python function:

```text
run_show_command()
```

That tool has a clear job:

- Load the testbed.
- Connect to the device.
- Run a command.
- Return output.
- Log the tool call.
- Disconnect.

Small tools are easier to test, explain, and trust.

## Why the LLM Does Not Know the Network Unless We Give It Tools

An LLM does not automatically know your router's current interface status. It may know what Cisco commands look like, and it may understand network concepts, but it does not have live access to your lab unless you provide a tool.

That distinction matters.

The model can reason about observations, but the tool must collect the observations first. In Episode 1, Avi does not need a real LLM yet because we are proving the tool path before adding reasoning on top.

## Why Logs Matter

Logs are accountability. They tell us what happened, when it happened, which device was touched, which command was used, and whether the tool succeeded or failed.

If Avi touches the network, we record it.

Episode 1 writes JSON Lines to:

```text
avi_tool_log.jsonl
```

This is intentionally simple. Later episodes can improve the black box recorder, but the habit starts here.
