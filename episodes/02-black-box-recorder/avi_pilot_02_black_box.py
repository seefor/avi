"""
Episode 2: Building Avi - The Black Box Recorder.

This starter script keeps the Episode 1 behavior small and read-only, then adds
a reusable JSON Lines recorder for tool calls.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pyats.topology import loader
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


TESTBED_FILE = "testbed.yaml"
LOG_FILE = "avi_black_box.jsonl"
DEFAULT_DEVICE = "Cat9k_AO_Sandbox"
DEFAULT_COMMAND = "show ip interface brief"
DEFAULT_MISSION = "Hey Avi, check Cat9k_AO_Sandbox and record the flight."
ALLOWED_COMMANDS = {"show ip interface brief", "show version"}

console = Console()


@dataclass
class ToolRecord:
    timestamp: str
    event: str
    tool_name: str
    device_name: str
    command: str
    status: str
    duration_ms: int | None = None
    summary: dict[str, Any] | None = None
    error: str | None = None


class BlackBoxRecorder:
    """Append-only JSON Lines recorder for Avi tool activity."""

    def __init__(self, log_file: str = LOG_FILE) -> None:
        self.log_path = Path(log_file)

    def write(self, record: ToolRecord) -> None:
        with self.log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(asdict(record)) + "\n")

    def recent(self, limit: int = 5) -> list[dict[str, Any]]:
        if not self.log_path.exists():
            return []

        lines = self.log_path.read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines[-limit:]]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def validate_command(command: str) -> None:
    if command not in ALLOWED_COMMANDS:
        allowed = ", ".join(sorted(ALLOWED_COMMANDS))
        raise ValueError(f"Command not allowed in Episode 2: {command}. Allowed: {allowed}")


def load_testbed(testbed_file: str = TESTBED_FILE):
    path = Path(testbed_file)
    if not path.exists():
        raise FileNotFoundError(f"Missing {testbed_file}. Copy testbed.example.yaml to testbed.yaml first.")
    return loader.load(str(path))


def summarize_interface_status(raw_output: str) -> dict[str, int]:
    summary = {"interfaces_found": 0, "up": 0, "down": 0, "administratively_down": 0}

    for line in raw_output.splitlines():
        cleaned = line.strip().lower()
        if not cleaned or cleaned.startswith("interface "):
            continue
        if "administratively down" in cleaned:
            summary["interfaces_found"] += 1
            summary["administratively_down"] += 1
        elif " down " in f" {cleaned} ":
            summary["interfaces_found"] += 1
            summary["down"] += 1
        elif " up " in f" {cleaned} ":
            summary["interfaces_found"] += 1
            summary["up"] += 1

    return summary


def run_recorded_show_command(device_name: str, command: str, recorder: BlackBoxRecorder) -> tuple[str, dict[str, int]]:
    validate_command(command)
    device = None
    start = time.perf_counter()

    recorder.write(
        ToolRecord(
            timestamp=utc_now(),
            event="tool_start",
            tool_name="pyats_show_command",
            device_name=device_name,
            command=command,
            status="started",
        )
    )

    try:
        testbed = load_testbed()
        device = testbed.devices[device_name]
        device.connect(via="cli", log_stdout=False, learn_hostname=True, init_exec_commands=[], init_config_commands=[])
        output = device.execute(command)
        summary = summarize_interface_status(output)
        duration_ms = int((time.perf_counter() - start) * 1000)

        recorder.write(
            ToolRecord(
                timestamp=utc_now(),
                event="tool_finish",
                tool_name="pyats_show_command",
                device_name=device_name,
                command=command,
                status="success",
                duration_ms=duration_ms,
                summary=summary,
            )
        )
        return output, summary

    except Exception as error:
        duration_ms = int((time.perf_counter() - start) * 1000)
        recorder.write(
            ToolRecord(
                timestamp=utc_now(),
                event="tool_finish",
                tool_name="pyats_show_command",
                device_name=device_name,
                command=command,
                status="failure",
                duration_ms=duration_ms,
                error=str(error),
            )
        )
        raise

    finally:
        if device is not None and getattr(device, "connected", False):
            device.disconnect()


def print_recent_records(recorder: BlackBoxRecorder) -> None:
    table = Table(title="Recent Avi Black Box Records")
    table.add_column("Event")
    table.add_column("Device")
    table.add_column("Command")
    table.add_column("Status")
    table.add_column("Duration")

    for record in recorder.recent():
        table.add_row(
            record.get("event", ""),
            record.get("device_name", ""),
            record.get("command", ""),
            record.get("status", ""),
            str(record.get("duration_ms") or ""),
        )

    console.print(table)


def main() -> None:
    recorder = BlackBoxRecorder()
    console.print(Panel(DEFAULT_MISSION, title="Avi Mission", border_style="cyan"))
    _, summary = run_recorded_show_command(DEFAULT_DEVICE, DEFAULT_COMMAND, recorder)

    report = (
        "Avi Black Box Report\n"
        f"Device: {DEFAULT_DEVICE}\n"
        f"Command: {DEFAULT_COMMAND}\n\n"
        f"Interfaces found: {summary['interfaces_found']}\n"
        f"Up interfaces: {summary['up']}\n"
        f"Down interfaces: {summary['down']}\n"
        f"Administratively down interfaces: {summary['administratively_down']}\n\n"
        f"Recorder file: {LOG_FILE}"
    )
    console.print(Panel(report, title="Report", border_style="green"))
    print_recent_records(recorder)


if __name__ == "__main__":
    main()
