# Building Avi: First Flight with pyATS SSH

In Episode 1, Avi takes a very small first flight.

The goal is to connect to one Cisco IOS-XE Cat9k sandbox device using pyATS and Unicon over SSH, run one approved read-only command, return a basic report, and log the tool call.

No LLM API is required yet. No configuration changes are allowed. Avi is just learning how to use one reliable network instrument.

## Avi Flight Rules for Episode 1

Before we run anything, Avi has a few rules:

1. Read-only commands only.
2. No configuration mode.
3. No autonomous decisions.
4. Log every tool call.
5. A human reviews the result before any action is taken.

These rules are not limitations. They are how we build trust.

## Lab Device

Episode 1 is written against a Cisco IOS-XE Cat9k sandbox device:

- Device name: `Cat9k_AO_Sandbox`
- OS: `iosxe`
- Management IP: `10.10.20.66`
- Protocol: SSH
- Default command: `show ip interface brief`

The running configuration for this device includes SSH access on the VTY lines, NETCONF, and RESTCONF. Episode 1 only uses SSH and read-only CLI commands. NETCONF and RESTCONF are useful later, but they are intentionally out of scope for the first flight.

## Architecture

```text
User Prompt -> Avi -> pyATS Tool -> SSH -> Cat9k Sandbox -> show ip interface brief -> Report
```

That flow is the beginning of agentic network automation. In Episode 1, the tool choice is still fixed on purpose. Avi receives a mission, runs one approved read-only tool, checks the network, and reports back with evidence.

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

- Username
- Password
- Enable password, if your sandbox requires one
- Device IP address, if your lab address is different

The real `testbed.yaml` is ignored by Git because it may contain lab credentials.

Do not paste encrypted password strings from a running config into `testbed.yaml`. pyATS needs the actual SSH username and password you use to access the device.

## Run the First Flight

```bash
python avi_pilot_01_pyats.py
```

The default mission is:

```text
Hey Avi, check Cat9k_AO_Sandbox and tell me if any interfaces are down.
```

## Expected Output

Your exact interface names and statuses will depend on your lab device, but the output should look similar to this:

```text
Avi Mission
Hey Avi, check Cat9k_AO_Sandbox and tell me if any interfaces are down.

Avi First Flight Report
Device: Cat9k_AO_Sandbox
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
- Run an approved read-only show command.
- Build a tiny tool function around network access.
- Summarize raw CLI output into a simple report.
- Log what Avi did.
- Keep safety boundaries visible in the code.

That log is Avi's first black box recorder. It is simple, but it starts the habit that matters: when automation touches the network, we keep evidence.

## Homework

1. Change the device IP.
2. Add a second approved read-only command.
3. Try `show version`.
4. Look at the tool log.
5. Do not add config changes yet.
