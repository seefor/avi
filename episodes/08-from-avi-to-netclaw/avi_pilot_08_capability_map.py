"""
Episode 8: Building Avi - From Avi to NetClaw.

This capstone script maps Avi's first-series building blocks into a larger
assistant capability model.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


class Capability(BaseModel):
    episode: int
    name: str
    capability_type: Literal["tool", "evidence", "state", "structure", "scale", "intent", "control", "direction"]
    what_it_gives_avi: str
    why_it_matters: str


def build_capability_map() -> list[Capability]:
    return [
        Capability(episode=1, name="First Flight with pyATS SSH", capability_type="tool", what_it_gives_avi="One approved read-only network tool.", why_it_matters="Reliable tools come before agent behavior."),
        Capability(episode=2, name="The Black Box Recorder", capability_type="evidence", what_it_gives_avi="A record of tool activity.", why_it_matters="Trust requires evidence."),
        Capability(episode=3, name="Teaching Avi to Read Network State", capability_type="state", what_it_gives_avi="Interface state objects.", why_it_matters="Operators need state, not just raw output."),
        Capability(episode=4, name="Structured Output and Parsing", capability_type="structure", what_it_gives_avi="Validated JSON reports.", why_it_matters="Other systems need predictable data."),
        Capability(episode=5, name="Multi-Device Observation", capability_type="scale", what_it_gives_avi="Fleet-level reporting patterns.", why_it_matters="Real operations span more than one device."),
        Capability(episode=6, name="Source of Truth", capability_type="intent", what_it_gives_avi="Intent vs observation comparison.", why_it_matters="Correctness requires knowing intended state."),
        Capability(episode=7, name="Human-in-the-Loop Safety", capability_type="control", what_it_gives_avi="Approval records.", why_it_matters="Humans stay in control of risky decisions."),
        Capability(episode=8, name="From Avi to NetClaw", capability_type="direction", what_it_gives_avi="A larger architecture map.", why_it_matters="The series becomes a foundation, not a one-off demo."),
    ]


def print_capability_map(capabilities: list[Capability]) -> None:
    table = Table(title="Avi Capability Map")
    table.add_column("Ep")
    table.add_column("Capability")
    table.add_column("Type")
    table.add_column("Gives Avi")
    table.add_column("Why It Matters")

    for item in capabilities:
        table.add_row(
            str(item.episode),
            item.name,
            item.capability_type,
            item.what_it_gives_avi,
            item.why_it_matters,
        )

    console.print(table)


def main() -> None:
    console.print(Panel("Map Avi's first arc into the NetClaw direction.", title="Avi Mission", border_style="cyan"))
    capabilities = build_capability_map()
    print_capability_map(capabilities)

    closing = (
        "Avi is not NetClaw yet.\n\n"
        "Avi is the careful path: tools, evidence, state, structure, scale, intent, and control.\n"
        "That is the foundation for a network assistant we would actually trust."
    )
    console.print(Panel(closing, title="Closing Thought", border_style="green"))


if __name__ == "__main__":
    main()
