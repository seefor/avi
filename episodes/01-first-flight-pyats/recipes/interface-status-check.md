# Recipe: Check Interface Status on a Single Device

## Goal

Check interface status on one Cisco IOS-XE device and produce a basic human-readable summary.

## Input

- Device name: `core-r1`
- Testbed file: `testbed.yaml`
- User mission: "Hey Avi, check core-r1 and tell me if any interfaces are down."

## Tool Used

```text
run_show_command()
```

This tool loads the pyATS testbed, connects to the device over SSH, runs one command, logs the tool call, and disconnects.

## pyATS Command

```text
show ip interface brief
```

## Expected Output

A short report with counts similar to:

```text
Interfaces found: 6
Up interfaces: 2
Down interfaces: 3
Administratively down interfaces: 1
```

The exact numbers depend on your lab device.

## Safety Level

Read-only.

This recipe only runs a show command. It does not enter configuration mode and does not change the device.

## Future Improvement Ideas

- Add a second device from the same testbed.
- Store the raw command output in the tool log.
- Parse the command output into structured interface records.
- Compare current interface state against an expected baseline.
- Add human approval before any future remediation workflow.
