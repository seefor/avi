"""
Episode 7: Building Avi - Human-in-the-Loop Safety.

This starter script creates a recommendation packet and requires a human
review decision. It does not execute network changes.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel


OUTPUT_FILE = "avi_approval_record.json"
console = Console()


class RecommendationPacket(BaseModel):
    finding_id: str
    device_name: str
    finding_summary: str
    suggested_next_step: str
    risk_note: str
    required_decision: Literal["approve", "reject", "defer"] = "approve"


class ApprovalRecord(BaseModel):
    packet: RecommendationPacket
    decision: Literal["approve", "reject", "defer"]
    reviewer_note: str
    reviewed_at: str
    execution_allowed: bool


def build_sample_packet() -> RecommendationPacket:
    return RecommendationPacket(
        finding_id="finding-001",
        device_name="example-access-1",
        finding_summary="Observed state does not match intended state for one interface.",
        suggested_next_step="Open a review ticket and investigate the interface state.",
        risk_note="This packet is for review only. No network change will be executed.",
    )


def ask_for_decision() -> tuple[Literal["approve", "reject", "defer"], str]:
    console.print("Choose a review decision: approve, reject, or defer")
    raw_decision = input("Decision: ").strip().lower()

    if raw_decision not in {"approve", "reject", "defer"}:
        console.print("Invalid decision. Defaulting to defer.")
        raw_decision = "defer"

    note = input("Reviewer note: ").strip() or "No note provided."
    return raw_decision, note  # type: ignore[return-value]


def build_approval_record(packet: RecommendationPacket, decision: str, note: str) -> ApprovalRecord:
    return ApprovalRecord(
        packet=packet,
        decision=decision,  # type: ignore[arg-type]
        reviewer_note=note,
        reviewed_at=datetime.now(timezone.utc).isoformat(),
        execution_allowed=False,
    )


def save_record(record: ApprovalRecord, output_file: str = OUTPUT_FILE) -> None:
    Path(output_file).write_text(record.model_dump_json(indent=2), encoding="utf-8")


def main() -> None:
    packet = build_sample_packet()
    console.print(Panel(packet.model_dump_json(indent=2), title="Avi Recommendation Packet", border_style="cyan"))

    decision, note = ask_for_decision()
    record = build_approval_record(packet, decision, note)
    save_record(record)

    console.print(Panel(record.model_dump_json(indent=2), title="Saved Approval Record", border_style="green"))
    console.print(f"Approval record written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
