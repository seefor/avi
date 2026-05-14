# Building Avi: First Flight with pyATS SSH

In Episode 1, Avi takes a very small first flight.

The goal is to connect to one Cisco IOS-XE lab device using pyATS and Unicon over SSH, run one read-only command, return a basic report, and log the tool call.

No LLM API is required yet. No configuration changes are allowed. Avi is just learning how to use one reliable network instrument.

## Architecture

```text
User Prompt -> Avi -> pyATS Tool -> SSH -> Router -> show ip interface brief -> Report
```

That flow is the beginning of agentic network automation. A user asks for something, Avi chooses a tool, the tool checks the network, and Avi reports back with evidence.

## Setup on macOS or Linux

From this episode folder:

```bash
cd episodes/01-first-flight-pyats
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Setup on Windows

From this episode folder:

```powershell
cd episodes\01-first-flight-pyats
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the virtual environment again.

## Create Your Local Testbed

Copy the example testbed:

```bash
cp testbed.example.yaml testbed.yaml
```

On Windows PowerShell:

```powershell
Copy-Item testbed.example.yaml testbed.yaml
```

Now edit `testbed.yaml` and update:

- Device IP address
- Username
- Password
- Enable password

The real `testbed.yaml` is ignored by Git because it may contain lab credentials.

## Run the First Flight

```bash
python avi_pilot_01_pyats.py
```

The default mission is:

```text
Hey Avi, check core-r1 and tell me if any interfaces are down.
```

## Expected Output

Your exact interface names and statuses will depend on your lab device, but the output should look similar to this:

```text
Avi Mission
Hey Avi, check core-r1 and tell me if any interfaces are down.

Avi First Flight Report
Device: core-r1
Command: show ip interface brief

Interfaces found: 6
Up interfaces: 2
Down interfaces: 3
Administratively down interfaces: 1

Basic read:
Some interfaces appear to be down. Review the raw command output before taking action.

Tool call logged to avi_tool_log.jsonl
```

## What You Learned

In this episode, you learned how to:

- Describe a network device in a pyATS testbed.
- Connect to Cisco IOS-XE over SSH using pyATS and Unicon.
- Run a read-only show command.
- Build a tiny tool function around network access.
- Summarize raw CLI output into a simple report.
- Log what Avi did.

That log is Avi's first black box recorder. It is simple, but it starts the habit that matters: when automation touches the network, we keep evidence.

## Homework

1. Change the device IP.
2. Add a second device.
3. Try `show version`.
4. Look at the tool log.
5. Do not add config changes yet.
