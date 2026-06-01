# Avi

Avi is a lightweight educational network agent built for network engineers who want to learn agentic automation one careful step at a time.

This repository supports the YouTube series **"Avi"**. The long-term direction is to build toward a larger NetClaw-style network automation assistant, but we are not trying to build the whole production system on day one. Avi starts small, stays understandable, and adds capability only when the foundation is solid.

> Good agents are built on boring tools that work.

## What Avi Is

Avi is a build-in-public network assistant project.

It is not starting with autonomy. It is starting with trust.

Each episode adds one safe capability: observe, report, log, explain, structure, scale, compare, recommend, request approval, and only later act.

By the end of this first arc, Avi should feel less like a demo script and more like the early skeleton of a real network assistant.

## What Avi Is Not

Avi is not a generic AI agent tutorial.

Avi is not a chatbot-first project.

Avi is not a "let the AI configure the network" demo.

Avi is not NetClaw yet.

Avi is the careful path toward a network assistant we would actually trust near real infrastructure.

## How Avi Is Different From the Workshop

The AI Networking Workshop teaches the concepts of LLMs, prompts, memory, and agents in a classroom format.

Avi is different: Avi is the build-in-public story of turning those ideas into a trusted network assistant, one safe capability at a time.

The workshop is the classroom.

Avi is the build.

## Series Philosophy

The Avi series is built around a simple idea: do not give an assistant more power until it has earned more trust.

That means the early episodes intentionally avoid flashy shortcuts. Avi starts with read-only access, clear logs, structured state, source-of-truth comparison, and human approval gates before anything resembling autonomy enters the picture.

The point is not to make Avi impressive on day one.

The point is to make Avi understandable, observable, and safe enough to grow.

## Episode Roadmap

| Episode | Title | What Avi Learns | Folder |
|---|---|---|---|
| 1 | First Flight with pyATS SSH | Connect to one IOS-XE Cat9k sandbox, run one approved read-only command, summarize the result, and log the tool call. | `episodes/01-first-flight-pyats` |
| 2 | The Black Box Recorder | Turn simple tool logging into a reusable evidence trail with timing, status, summary, and error details. | `episodes/02-black-box-recorder` |
| 3 | Teaching Avi to Read Network State | Convert raw CLI output into simple interface state objects a human can review. | `episodes/03-teaching-avi-to-read-network-state` |
| 4 | Structured Output and Parsing | Produce validated JSON reports that other tools and workflows can consume. | `episodes/04-structured-output-and-parsing` |
| 5 | Multi-Device Observation | Roll up observations across multiple devices while keeping per-device evidence visible. | `episodes/05-multi-device-observation` |
| 6 | Source of Truth | Compare intended state against observed state and report drift for review. | `episodes/06-source-of-truth` |
| 7 | Human-in-the-Loop Safety | Create recommendation packets and approval records while keeping execution disabled. | `episodes/07-human-in-the-loop-safety` |
| 8 | From Avi to NetClaw | Map the first Avi arc into the larger NetClaw direction and assistant maturity model. | `episodes/08-from-avi-to-netclaw` |

## Repository Layout

```text
avi/
├── README.md
├── episodes/
│   ├── 01-first-flight-pyats/
│   ├── 02-black-box-recorder/
│   ├── 03-teaching-avi-to-read-network-state/
│   ├── 04-structured-output-and-parsing/
│   ├── 05-multi-device-observation/
│   ├── 06-source-of-truth/
│   ├── 07-human-in-the-loop-safety/
│   └── 08-from-avi-to-netclaw/
└── .gitignore
```

Each episode folder includes a README. Most episodes also include a starter script, requirements file, and a camera-ready walkthrough under `docs/`.

## Quick Start

Clone the repo:

```bash
git clone https://github.com/seefor/avi.git
cd avi
```

Start with Episode 1:

```bash
cd episodes/01-first-flight-pyats
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp testbed.example.yaml testbed.yaml
python avi_pilot_01_pyats.py
```

On Windows PowerShell:

```powershell
cd episodes\01-first-flight-pyats
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item testbed.example.yaml testbed.yaml
python avi_pilot_01_pyats.py
```

Edit your local `testbed.yaml` with the real SSH details for your lab device. The real `testbed.yaml` is ignored by Git.

## Lab Safety Model

Avi's first arc follows a trust-first safety model:

1. Read-only commands first.
2. No configuration mode in the early episodes.
3. No autonomous decisions.
4. Every tool call should leave evidence.
5. Structured output should be validated before other systems rely on it.
6. Source-of-truth comparison should produce review findings, not automatic changes.
7. Human approval must exist before any risky action is considered.

This is intentional. The series is not trying to make the assistant powerful as quickly as possible. It is trying to make the assistant trustworthy enough to grow.

## Episode 1 Lab Device

Episode 1 is written against a Cisco IOS-XE Cat9k sandbox device:

- Device name: `Cat9k_AO_Sandbox`
- OS: `iosxe`
- Management IP: `10.10.20.66`
- Protocol: SSH
- Default command: `show ip interface brief`

Do not commit real credentials, running configs, or secrets. Use the example files as templates and keep real lab details in ignored local files.

## Generated Files

Some episodes write local output files while you run the labs. These are ignored by Git:

- `testbed.yaml`
- `avi_tool_log.jsonl`
- `avi_black_box.jsonl`
- `avi_interface_report.json`
- `avi_approval_record.json`

## Recommended Learning Path

Run the episodes in order.

Do not skip straight to the later ideas. The value of Avi is the progression:

```text
Tool -> Evidence -> State -> Structure -> Scale -> Intent -> Approval -> Direction
```

That path is what keeps the project different from a generic AI agent demo.

## The North Star

Avi is not about building a flashy AI agent.

Avi is about earning the right to automate the network.

The long-term NetClaw direction can become more capable, more connected, and more intelligent, but the foundation stays the same: reliable tools, observable behavior, structured state, clear intent, and human control where it matters.
