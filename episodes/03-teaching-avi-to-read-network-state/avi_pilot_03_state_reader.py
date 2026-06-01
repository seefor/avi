"""
Episode 3: Building Avi - Teaching Avi to Read Network State.

This starter script keeps Avi read-only and teaches it to turn
`show ip interface brief` output into simple interface state objects.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pyats.topology import loader
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


TESTBED_FILE = "testbed.yaml"
DEFAULT_DEVICE = "Cat9k_AO_Sandbox"
DEFAULT_COMMAND = "show ip interface brief"
ALLOWED_COMMANDS = {"show ip interface brief", "show version"}

console = Console()


@dataclass
class InterfaceState:
    name: str
    ip_address: str
    status: str
    protocol: str
    state_label: str
    review_note: str


def validate_command(command: str) -> None:
    if command not in ALLOWED_COMMANDS:
        allowed = ", ".join(sorted(ALLOWED_COMMANDS))
        raise ValueError(f"Command not allowed in Episode 3: {command}. Allowed: {allowed}")


def load_testbed(testbed_file: str = TESTBED_FILE):
    path = Path(testbed_file)
    if not path.exists():
        raise FileNotFoundError(f"Missing {testbed_file}. Copy testbed.example.yaml to testbed.yaml first.")
    return loader.load(str(path))


def run_show_command(device_name: str, command: str) -> str:
    validate_command(command)
    testbed = load_testbed()
    device = testbed.devices[device_name]

    try:
        device.connect(via="cli", log_stdout=False, learn_hostname=True, init_exec_commands=[], init_config_commands=[])
        return device.execute(command)
    finally:
        if getattr(device, "connected", False):
            device.disconnect()


def classify_interface(status: str, protocol: str) -> tuple[str, str]:
    status_l = status.lower()
    protocol_l = protocol.lower()

    if "administratively" in status_l:
        return "admin_down", "Configured shutdown. Confirm whether this is intentional."
    if status_l == "up" and protocol_l == "up":
        return "healthy", "Interface appears operational."
    if status_l == "down" or protocol_l == "down":
        return "down", "Interface is down. Review cabling, peer state, or intended design."
    return "unknown", "Avi could not confidently classify this state. Review raw output."


def parse_show_ip_interface_brief(raw_output: str) -> list[InterfaceState]:
    interfaces: list[InterfaceState] = []

    for line in raw_output.splitlines():
        stripped = line.strip()
        if not stripped or stripped.lower().startswith("interface "):
            continue

        parts = stripped.split()
        if len(parts) < 6:
            continue

        name = parts[0]
        ip_address = parts[1]
        protocol = parts[-1]
        status = " ".join(parts[4:-1])
        state_label, review_note = classify_interface(status, protocol)

        interfaces.append(
            InterfaceState(
                name=name,
                ip_address=ip_address,
                status=status,
                protocol=protocol,
                state_label=state_label,
                review_note=review_note,
            )
        )

    return interfaces


def print_state_table(interfaces: list[InterfaceState]) -> None:
    table = Table(title="Avi Interface State Review")
    table.add_column("Interface")
    table.add_column("IP Address")
    table.add_column("Status")
    table.add_column("Protocol")
    table.add_column("State")
    table.add_column("Review Note")

    for interface in interfaces:
        table.add_row(
            interface.name,
            interface.ip_address,
            interface.status,
            interface.protocol,
            interface.state_label,
            interface.review_note,
        )

    console.print(table)


def main() -> None:
    mission = "Hey Avi, read the interface state from Cat9k_AO_Sandbox."
    console.print(Panel(mission, title="Avi Mission", border_style="cyan"))

    raw_output = run_show_command(DEFAULT_DEVICE, DEFAULT_COMMAND)
    interfaces = parse_show_ip_interface_brief(raw_output)

    summary = {
        "total": len(interfaces),
        "healthy": sum(1 for item in interfaces if item.state_label == "healthy"),
        "down": sum(1 for item in interfaces if item.state_label == "down"),
        "admin_down": sum(1 for item in interfaces if item.state_label == "admin_down"),
        "unknown": sum(1 for item in interfaces if item.state_label == "unknown"),
    }

    report = (
        "Avi State Reader Report\n"
        f"Device: {DEFAULT_DEVICE}\n"
        f"Command: {DEFAULT_COMMAND}\n\n"
        f"Interfaces reviewed: {summary['total']}\n"
        f"Healthy: {summary['healthy']}\n"
        f"Down: {summary['down']}\n"
        f"Administratively down: {summary['admin_down']}\n"
        f"Unknown: {summary['unknown']}\n"
    )

    console.print(Panel(report, title="Report", border_style="green"))
    print_state_table(interfaces)


if __name__ == "__main__":
    main()
