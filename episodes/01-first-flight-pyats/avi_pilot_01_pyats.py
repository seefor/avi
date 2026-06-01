"""
Episode 1: Building Avi - First Flight with pyATS SSH.

This script is intentionally small and beginner-friendly. Avi is not a full
agent yet. For now, Avi has one read-only tool that connects to a Cisco IOS-XE
device, runs an approved show command, prints a basic report, and logs the tool
call.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pyats.topology import loader
from rich.console import Console
from rich.panel import Panel


TESTBED_FILE = "testbed.yaml"
LOG_FILE = "avi_tool_log.jsonl"
DEFAULT_DEVICE = "core-r1"
DEFAULT_COMMAND = "show ip interface brief"
DEFAULT_MISSION = "Hey Avi, check core-r1 and tell me if any interfaces are down."

# Episode 1 is intentionally read-only. This allowlist makes the safety boundary
# visible in code instead of relying only on narration or prompt wording.
ALLOWED_COMMANDS = {
    "show ip interface brief",
    "show version",
}

console = Console()


def log_tool_call(
    *,
    tool_name: str,
    device_name: str,
    command: str,
    status: str,
    details: dict[str, Any] | None = None,
    log_file: str = LOG_FILE,
) -> None:
    """Write one tool call record to Avi's simple black box recorder."""
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool_name": tool_name,
        "device_name": device_name,
        "command": command,
        "status": status,
        "details": details or {},
    }

    with Path(log_file).open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")


def load_testbed(testbed_file: str = TESTBED_FILE):
    """Load the pyATS testbed file that describes the lab devices."""
    testbed_path = Path(testbed_file)

    if not testbed_path.exists():
        raise FileNotFoundError(
            f"Could not find {testbed_file}. Copy testbed.example.yaml to "
            f"{testbed_file}, then edit it for your lab."
        )

    return loader.load(str(testbed_path))


def validate_command(command: str) -> None:
    """Stop Episode 1 from running commands outside the approved read-only list."""
    if command not in ALLOWED_COMMANDS:
        allowed = ", ".join(sorted(ALLOWED_COMMANDS))
        raise ValueError(
            f"Command not allowed in Episode 1: {command}. "
            f"Allowed commands: {allowed}"
        )


def run_show_command(
    device_name: str,
    command: str,
    testbed_file: str = TESTBED_FILE,
) -> str:
    """Connect to one device with pyATS, run an approved show command, and return output."""
    device = None

    try:
        validate_command(command)
        testbed = load_testbed(testbed_file)

        if device_name not in testbed.devices:
            available_devices = ", ".join(testbed.devices.keys()) or "none"
            raise ValueError(
                f"Device '{device_name}' was not found in {testbed_file}. "
                f"Available devices: {available_devices}"
            )

        device = testbed.devices[device_name]

        # Unicon handles the SSH session for pyATS. The init command lists are
        # empty so Episode 1 stays read-only and does not enter configuration mode.
        device.connect(
            via="cli",
            log_stdout=False,
            learn_hostname=True,
            init_exec_commands=[],
            init_config_commands=[],
        )

        output = device.execute(command)

        log_tool_call(
            tool_name="pyats_show_command",
            device_name=device_name,
            command=command,
            status="success",
            details={"output_length": len(output)},
        )

        return output

    except Exception as error:
        log_tool_call(
            tool_name="pyats_show_command",
            device_name=device_name,
            command=command,
            status="failure",
            details={"error": str(error)},
        )
        raise

    finally:
        if device is not None and getattr(device, "connected", False):
            device.disconnect()


def summarize_interface_status(raw_output: str) -> dict[str, int]:
    """Create a lightweight summary from show ip interface brief output."""
    summary = {
        "interfaces_found": 0,
        "up": 0,
        "down": 0,
        "administratively_down": 0,
    }

    for line in raw_output.splitlines():
        cleaned_line = line.strip().lower()

        # Skip headers and blank lines.
        if not cleaned_line or cleaned_line.startswith("interface "):
            continue

        if "administratively down" in cleaned_line:
            summary["interfaces_found"] += 1
            summary["administratively_down"] += 1
        elif " down " in f" {cleaned_line} ":
            summary["interfaces_found"] += 1
            summary["down"] += 1
        elif " up " in f" {cleaned_line} ":
            summary["interfaces_found"] += 1
            summary["up"] += 1

    return summary


def avi_report(prompt: str, device_name: str = DEFAULT_DEVICE) -> str:
    """
    Run Avi's first mission and return a human-readable report.

    The full agentic version will come later. In Episode 1, the "prompt" is
    printed for the human, and the script always uses the same safe read-only
    command.
    """
    console.print(Panel(prompt, title="Avi Mission", border_style="cyan"))

    raw_output = run_show_command(device_name, DEFAULT_COMMAND)
    summary = summarize_interface_status(raw_output)

    if summary["down"] or summary["administratively_down"]:
        basic_read = (
            "Some interfaces appear to be down. Review the raw command output "
            "before taking action."
        )
    else:
        basic_read = "No down interfaces were detected in the basic summary."

    report = (
        "Avi First Flight Report\n"
        f"Device: {device_name}\n"
        f"Command: {DEFAULT_COMMAND}\n\n"
        f"Interfaces found: {summary['interfaces_found']}\n"
        f"Up interfaces: {summary['up']}\n"
        f"Down interfaces: {summary['down']}\n"
        "Administratively down interfaces: "
        f"{summary['administratively_down']}\n\n"
        f"Basic read:\n{basic_read}\n\n"
        f"Tool call logged to {LOG_FILE}"
    )

    return report


def main() -> None:
    """Start Avi's first flight from the command line."""
    try:
        report = avi_report(DEFAULT_MISSION)
        console.print(Panel(report, title="Report", border_style="green"))

    except Exception as error:
        console.print(Panel(str(error), title="First Flight Failed", border_style="red"))
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
