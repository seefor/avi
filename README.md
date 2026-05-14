# Avi

Avi is a lightweight educational network agent built for network engineers who want to learn agentic automation one careful step at a time.

This repository supports the YouTube series **"Avi"**. The long-term direction is to build toward a larger NetClaw-style network automation assistant, but we are not trying to build the whole production system on day one. Avi starts small, stays understandable, and adds capability only when the foundation is solid.

Series philosophy:

> Good agents are built on boring tools that work.

In Episode 1, Avi is just a tiny pilot with one instrument: a pyATS SSH tool that connects to a Cisco IOS-XE lab device, runs one read-only command, prints a basic report, and writes down what happened in a simple tool log.

## What Episode 1 Builds

Episode 1 builds a beginner-friendly pyATS workflow:

- A `testbed.yaml` file that describes one Cisco IOS-XE device.
- A Python script that loads the testbed with pyATS.
- A Unicon SSH connection through pyATS.
- One read-only command: `show ip interface brief`.
- A small report that summarizes interface state.
- A JSON Lines tool log that acts like Avi's first black box recorder.

The goal is not magic. The goal is trust. Before Avi can become an agent, it needs a reliable way to touch the network, observe state, and record what it did.

## What Episode 1 Does Not Do Yet

Episode 1 is intentionally small. It does not:

- Use Netmiko.
- Use a real LLM API.
- Configure devices.
- Enter configuration mode.
- Run `conf t`.
- Make changes to the network.
- Parse output with a full structured parser.
- Use a source of truth.
- Make autonomous decisions.

That restraint is the point. Read-only observation comes first.

## Series Roadmap

1. First Flight with pyATS SSH
2. Teaching Avi to Read Network State
3. Structured Output and Parsing
4. The Black Box Recorder
5. Human-in-the-Loop Safety
6. Source of Truth
7. From Avi to NetClaw

Each episode adds one useful building block. By the end, Avi should feel less like a demo script and more like the early skeleton of a real network assistant.
