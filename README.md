# Avi

Avi is a lightweight educational network agent built for network engineers who want to learn agentic automation one careful step at a time.

This repository supports the YouTube series **"Avi"**. The long-term direction is to build toward a larger NetClaw-style network automation assistant, but we are not trying to build the whole production system on day one. Avi starts small, stays understandable, and adds capability only when the foundation is solid.

## What Avi Is

Avi is a build-in-public network assistant project.

It is not starting with autonomy. It is starting with trust.

Each episode adds one safe capability: observe, report, log, explain, compare, recommend, request approval, and only later act.

## What Avi Is Not

Avi is not a generic AI agent tutorial. Avi is not a chatbot-first project. Avi is not a "let the AI configure the network" demo. Avi is not NetClaw yet.

Avi is the careful path toward a network assistant we would actually trust near real infrastructure.

## How Avi Is Different From the Workshop

The AI Networking Workshop teaches the concepts of LLMs, prompts, memory, and agents in a classroom format.

Avi is different: Avi is the build-in-public story of turning those ideas into a trusted network assistant, one safe capability at a time.

## Series Philosophy

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
2. The Black Box Recorder
3. Teaching Avi to Read Network State
4. Structured Output and Parsing
5. Multi-Device Observation
6. Source of Truth
7. Human-in-the-Loop Safety
8. From Avi to NetClaw

Each episode adds one useful building block. By the end, Avi should feel less like a demo script and more like the early skeleton of a real network assistant.
