"""
Episode 4: Building Avi - Structured Output and Parsing.

This starter script uses clearly fake sample interface observations and turns
them into a validated JSON report. The focus is data shape and validation.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


OUTPUT_FILE = "avi_interface_report.json"
SCHEMA_VERSION = "avi.interface_report.v1"

console = Console()


class InterfaceRecord(BaseModel):
    name: str
    ip_address: str
    status: str
    protocol: str
    state_label: Literal["healthy", "down", "admin_down", "unknown"]
    review_note: str


class InterfaceSummary(BaseModel):
    total: int = 0
    healthy: int = 0
    down: int = 0
    admin_down: int = 0
    unknown: int = 0


class AviInterfaceReport(BaseModel):
    schema_version: str = Field(default=SCHEMA_VERSION)
    generated_at: str
    device_name: str
    command: str
    interfaces: list[InterfaceRecord]
    summary: InterfaceSummary


def sample_interface_records() -> list[InterfaceRecord]:
    return [
        InterfaceRecord(
            name="ExampleInterface0",
            ip_address="192.0.2.10",
            status="up",
            protocol="up",
            state_label="healthy",
            review_note="Sample interface appears operational.",
        ),
        InterfaceRecord(
            name="ExampleInterface1",
            ip_address="unassigned",
            status="administratively down",
            protocol="down",
            state_label="admin_down",
            review_note="Sample interface is configured down.",
        ),
    ]


def build_summary(interfaces: list[InterfaceRecord]) -> InterfaceSummary:
    return InterfaceSummary(
        total=len(interfaces),
        healthy=sum(1 for item in interfaces if item.state_label == "healthy"),
        down=sum(1 for item in interfaces if item.state_label == "down"),
        admin_down=sum(1 for item in interfaces if item.state_label == "admin_down"),
        unknown=sum(1 for item in interfaces if item.state_label == "unknown"),
    )


def build_report() -> AviInterfaceReport:
    interfaces = sample_interface_records()
    return AviInterfaceReport(
        generated_at=datetime.now(timezone.utc).isoformat(),
        device_name="example-device",
        command="show ip interface brief",
        interfaces=interfaces,
        summary=build_summary(interfaces),
    )


def save_report(report: AviInterfaceReport, output_file: str = OUTPUT_FILE) -> None:
    Path(output_file).write_text(report.model_dump_json(indent=2), encoding="utf-8")


def print_report(report: AviInterfaceReport) -> None:
    table = Table(title="Avi Structured Interface Report")
    table.add_column("Interface")
    table.add_column("IP")
    table.add_column("Status")
    table.add_column("Protocol")
    table.add_column("State")

    for interface in report.interfaces:
        table.add_row(interface.name, interface.ip_address, interface.status, interface.protocol, interface.state_label)

    console.print(table)
    console.print(Panel(json.dumps(report.summary.model_dump(), indent=2), title="Summary", border_style="green"))


def main() -> None:
    console.print(Panel("Build a validated JSON report for Avi.", title="Avi Mission", border_style="cyan"))
    report = build_report()
    save_report(report)
    print_report(report)
    console.print(f"Structured report written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
