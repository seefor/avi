# Episode 01 Walkthrough: First Flight with pyATS SSH

This walkthrough is written to be camera-ready. Use it as the spine for the episode, but keep the delivery natural.

## 1. Opening Hook

What to say:

"If we're going to build a network agent, the first thing it needs is not a giant brain. It needs one boring tool that works. Today Avi is going to connect to a router, run one read-only command, and tell us what it saw."

Teaching point:

- Agents are only useful when they have reliable tools.
- Episode 1 is about trust, not autonomy.

## 2. What We Are Building

What to say:

"This is Avi's first flight. The pilot is small. The instrument is pyATS. The mission is simple: check `core-r1` and tell me if any interfaces are down."

Architecture:

```text
User Prompt -> Avi -> pyATS Tool -> SSH -> Router -> show ip interface brief -> Report
```

Teaching point:

- We are not building the full NetClaw-style assistant yet.
- We are building the first safe building block.

## 3. Why pyATS

What to say:

"pyATS gives us a real network automation foundation. It understands testbeds, device connections, and network operating systems. Unicon handles the SSH session underneath pyATS, so our code can focus on the workflow."

Teaching points:

- pyATS testbeds describe the lab.
- Unicon handles CLI connection behavior.
- This episode does not use Netmiko.

## 4. Project Setup

Terminal commands:

```bash
cd episodes/01-first-flight-pyats
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Windows commands:

```powershell
cd episodes\01-first-flight-pyats
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

What to say:

"The virtual environment keeps this episode isolated. That matters when you're recording, teaching, or helping someone reproduce the lab."

Teaching point:

- Keep the demo environment predictable.

## 5. Testbed YAML

Terminal command:

```bash
cp testbed.example.yaml testbed.yaml
```

Windows command:

```powershell
Copy-Item testbed.example.yaml testbed.yaml
```

What to say:

"The testbed is Avi's map. It tells pyATS what device exists, how to reach it, and what credentials to use."

Fields to explain:

- `devices`: The devices in the lab.
- `core-r1`: The device name Avi will use.
- `os: iosxe`: The network operating system.
- `credentials`: Login and enable credentials.
- `connections.cli`: The SSH connection details.

Teaching point:

- Commit the example file.
- Do not commit the real `testbed.yaml`.

## 6. Building Avi's First Tool

What to say:

"Now we build the first real tool. It loads the testbed, finds the device, connects over SSH, runs `show ip interface brief`, logs what happened, and disconnects."

Functions to show:

- `log_tool_call()`
- `load_testbed()`
- `run_show_command()`
- `summarize_interface_status()`
- `avi_report()`

Teaching points:

- Keep network access inside a tool function.
- Use `finally` to disconnect.
- Log both success and failure.
- Keep the command read-only.

## 7. Running the First Flight

Terminal command:

```bash
python avi_pilot_01_pyats.py
```

What to say:

"This is not a chatbot yet. The script prints the mission, uses the pyATS tool, and returns a report. The agentic layer comes later."

Teaching point:

- A useful tool can exist before an LLM is involved.

## 8. Reading the Output

What to say:

"Avi is not making a change. It is reporting what it saw. If an interface is down, this is a signal for a human to investigate, not permission for automation to configure anything."

Expected shape:

```text
Interfaces found: 6
Up interfaces: 2
Down interfaces: 3
Administratively down interfaces: 1
```

Teaching point:

- Read-only summaries are a safe place to start.

## 9. The Tool Log

Terminal command:

```bash
cat avi_tool_log.jsonl
```

What to say:

"This is Avi's first black box recorder. Every time Avi touches the network, we want a record of the tool, device, command, status, and timestamp."

Teaching point:

- Logs create accountability.
- Logs help with troubleshooting.
- Logs become more important as the assistant gains more capability.

## 10. Wrap-Up

What to say:

"Today Avi learned one move: connect to a device, run a safe command, summarize the result, and record the flight. That is small, but it is the right kind of small."

Teaching point:

- Good agents are built from reliable, observable tool calls.

## 11. Homework

Ask viewers to:

1. Change the device IP.
2. Add a second device.
3. Try `show version`.
4. Look at the tool log.
5. Do not add config changes yet.

What to say:

"That last one is important. Keep Episode 1 read-only. We are building trust before we build power."

## 12. Tease Episode 2

What to say:

"In Episode 2, we'll start teaching Avi to read network state more carefully. The first flight proved we can reach the router. Next, we'll make the observation more useful."

Teaching point:

- Episode 2 moves from raw command output toward better network state understanding.
