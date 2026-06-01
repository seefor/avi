"""
Episode 5: Building Avi - Multi-Device Observation.

This starter script uses fake structured observations to teach multi-device
reporting without needing access to several real lab devices.
"""

from __future__ import annotations

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


class DeviceObservation(BaseModel):
    device_name: str
    interfaces_total: int
    healthy: int
    down: int
    admin_down: int
    unknown: int


class FleetSummary(BaseModel):
    devices_total: int
    interfaces_total: int
    healthy: int
    down: int
    admin_down: int
    unknown: int
    devices_needing_review: int


def sample_observations() -> list[DeviceObservation]:
    return [
        DeviceObservation(device_name="example-core-1", interfaces_total=8, healthy=5, down=1, admin_down=2, unknown=0),
        DeviceObservation(device_name="example-access-1", interfaces_total=12, healthy=7, down=2, admin_down=3, unknown=0),
        DeviceObservation(device_name="example-edge-1", interfaces_total=6, healthy=6, down=0, admin_down=0, unknown=0),
    ]


def build_fleet_summary(observations: list[DeviceObservation]) -> FleetSummary:
    return FleetSummary(
        devices_total=len(observations),
        interfaces_total=sum(item.interfaces_total for item in observations),
        healthy=sum(item.healthy for item in observations),
        down=sum(item.down for item in observations),
        admin_down=sum(item.admin_down for item in observations),
        unknown=sum(item.unknown for item in observations),
        devices_needing_review=sum(1 for item in observations if item.down or item.unknown),
    )


def print_device_table(observations: list[DeviceObservation]) -> None:
    table = Table(title="Avi Multi-Device Observation")
    table.add_column("Device")
    table.add_column("Interfaces")
    table.add_column("Healthy")
    table.add_column("Down")
    table.add_column("Admin Down")
    table.add_column("Unknown")

    for item in observations:
        table.add_row(
            item.device_name,
            str(item.interfaces_total),
            str(item.healthy),
            str(item.down),
            str(item.admin_down),
            str(item.unknown),
        )

    console.print(table)


def main() -> None:
    console.print(Panel("Review multiple device observations.", title="Avi Mission", border_style="cyan"))
    observations = sample_observations()
    summary = build_fleet_summary(observations)
    print_device_table(observations)

    report = (
        "Avi Fleet Summary\n"
        f"Devices reviewed: {summary.devices_total}\n"
        f"Interfaces reviewed: {summary.interfaces_total}\n"
        f"Healthy interfaces: {summary.healthy}\n"
        f"Down interfaces: {summary.down}\n"
        f"Admin down interfaces: {summary.admin_down}\n"
        f"Unknown interfaces: {summary.unknown}\n"
        f"Devices needing review: {summary.devices_needing_review}\n"
    )
    console.print(Panel(report, title="Fleet Report", border_style="green"))


if __name__ == "__main__":
    main()
