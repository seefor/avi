"""
Episode 6: Building Avi - Source of Truth.

This starter script compares simple intended state from YAML with sample
observed state. It reports drift for human review only.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


SOURCE_OF_TRUTH_FILE = "source_of_truth.example.yaml"
console = Console()


StateLabel = Literal["up", "down", "admin_down", "unknown"]


class InterfaceIntent(BaseModel):
    expected_state: StateLabel
    expected_ip: str


class InterfaceObservation(BaseModel):
    device_name: str
    interface_name: str
    observed_state: StateLabel
    observed_ip: str


class DriftFinding(BaseModel):
    device_name: str
    interface_name: str
    expected_state: StateLabel
    observed_state: StateLabel | str
    expected_ip: str
    observed_ip: str
    result: Literal["match", "drift", "missing_observation"]
    review_note: str


def load_intent(path: str = SOURCE_OF_TRUTH_FILE) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def sample_observed_state() -> list[InterfaceObservation]:
    return [
        InterfaceObservation(device_name="example-core-1", interface_name="ExampleInterface0", observed_state="up", observed_ip="192.0.2.10"),
        InterfaceObservation(device_name="example-core-1", interface_name="ExampleInterface1", observed_state="admin_down", observed_ip="unassigned"),
        InterfaceObservation(device_name="example-access-1", interface_name="ExampleInterface0", observed_state="up", observed_ip="192.0.2.20"),
        InterfaceObservation(device_name="example-access-1", interface_name="ExampleInterface1", observed_state="down", observed_ip="192.0.2.21"),
    ]


def compare_intent_to_observation(intent_data: dict, observations: list[InterfaceObservation]) -> list[DriftFinding]:
    observed_lookup = {(item.device_name, item.interface_name): item for item in observations}
    findings: list[DriftFinding] = []

    for device_name, device_data in intent_data.get("devices", {}).items():
        for interface_name, interface_data in device_data.get("interfaces", {}).items():
            intent = InterfaceIntent(**interface_data)
            observed = observed_lookup.get((device_name, interface_name))

            if observed is None:
                findings.append(
                    DriftFinding(
                        device_name=device_name,
                        interface_name=interface_name,
                        expected_state=intent.expected_state,
                        observed_state="missing",
                        expected_ip=intent.expected_ip,
                        observed_ip="missing",
                        result="missing_observation",
                        review_note="Intent exists, but Avi has no observation for this interface.",
                    )
                )
                continue

            matches = intent.expected_state == observed.observed_state and intent.expected_ip == observed.observed_ip
            findings.append(
                DriftFinding(
                    device_name=device_name,
                    interface_name=interface_name,
                    expected_state=intent.expected_state,
                    observed_state=observed.observed_state,
                    expected_ip=intent.expected_ip,
                    observed_ip=observed.observed_ip,
                    result="match" if matches else "drift",
                    review_note="Observed state matches intent." if matches else "Observed state does not match intent. Review before acting.",
                )
            )

    return findings


def print_findings(findings: list[DriftFinding]) -> None:
    table = Table(title="Avi Intent vs Observation Review")
    table.add_column("Device")
    table.add_column("Interface")
    table.add_column("Expected")
    table.add_column("Observed")
    table.add_column("Result")
    table.add_column("Review Note")

    for finding in findings:
        table.add_row(
            finding.device_name,
            finding.interface_name,
            f"{finding.expected_state} / {finding.expected_ip}",
            f"{finding.observed_state} / {finding.observed_ip}",
            finding.result,
            finding.review_note,
        )

    console.print(table)


def main() -> None:
    console.print(Panel("Compare intended state with observed state.", title="Avi Mission", border_style="cyan"))
    intent = load_intent()
    observations = sample_observed_state()
    findings = compare_intent_to_observation(intent, observations)
    print_findings(findings)

    drift_count = sum(1 for finding in findings if finding.result != "match")
    console.print(Panel(f"Findings needing review: {drift_count}", title="Summary", border_style="green"))


if __name__ == "__main__":
    main()
