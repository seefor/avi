"""
Episode 2: Building Avi - Giving Avi a Brain.

Avi gets a reasoning layer, but that layer is not allowed to operate tools.
This script uses sample evidence and a deterministic local brain simulator.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


class InterfaceEvidence(BaseModel):
    name: str
    state: Literal["up", "down", "admin_down", "unknown"]
    detail: str


class EvidenceReport(BaseModel):
    device_name: str
    observation: str
    interfaces: list[InterfaceEvidence]


class BrainResponse(BaseModel):
    summary: str
    review_items: list[str]
    evidence_used: list[str]
    safe_next_step: str
    boundary_reminder: str


BRAIN_RULES = """You are Avi, a cautious network operations assistant.

You may explain provided evidence.
You may suggest human review.
You may not operate tools.
You may not invent facts.
Use only the evidence provided.
"""


def build_sample_evidence() -> EvidenceReport:
    return EvidenceReport(
        device_name="example-device",
        observation="interface status review",
        interfaces=[
            InterfaceEvidence(name="ExampleInterface0", state="up", detail="Sample interface appears available."),
            InterfaceEvidence(name="ExampleInterface1", state="admin_down", detail="Sample interface is intentionally disabled."),
            InterfaceEvidence(name="ExampleInterface2", state="unknown", detail="Sample state needs review."),
        ],
    )


def build_prompt(report: EvidenceReport) -> str:
    return (
        f"{BRAIN_RULES}\n"
        "Task: Explain this evidence for a network engineer.\n"
        "Return a concise review summary.\n\n"
        f"Evidence:\n{report.model_dump_json(indent=2)}"
    )


def local_brain(report: EvidenceReport) -> BrainResponse:
    review_items = [item.name for item in report.interfaces if item.state in {"down", "admin_down", "unknown"}]
    evidence_used = [f"{item.name}: {item.state} - {item.detail}" for item in report.interfaces]

    if review_items:
        summary = f"Avi reviewed {len(report.interfaces)} interface records. {len(review_items)} item(s) need human review."
        safe_next_step = "Review the listed items and confirm whether the observed state is expected."
    else:
        summary = f"Avi reviewed {len(report.interfaces)} interface records. No review items were detected."
        safe_next_step = "No action is suggested from this evidence."

    return BrainResponse(
        summary=summary,
        review_items=review_items,
        evidence_used=evidence_used,
        safe_next_step=safe_next_step,
        boundary_reminder="Avi explained evidence only. Tool operation stayed outside the brain layer.",
    )


def print_evidence(report: EvidenceReport) -> None:
    table = Table(title="Structured Evidence for Avi's Brain")
    table.add_column("Interface")
    table.add_column("State")
    table.add_column("Detail")

    for item in report.interfaces:
        table.add_row(item.name, item.state, item.detail)

    console.print(table)


def main() -> None:
    console.print(Panel("Give Avi a brain, but keep tools outside the brain layer.", title="Avi Mission", border_style="cyan"))
    report = build_sample_evidence()
    prompt = build_prompt(report)
    response = local_brain(report)

    print_evidence(report)
    console.print(Panel(prompt, title="Prompt Template", border_style="blue"))
    console.print(Panel(response.model_dump_json(indent=2), title="Avi Brain Response", border_style="green"))


if __name__ == "__main__":
    main()
