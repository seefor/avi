# Avi Project Notes for AI Coding Assistants

Avi is an educational GitHub repository for a YouTube series about building a lightweight network agent step by step. The project is a learning path toward a larger NetClaw-style network automation assistant, but each episode should stay focused and beginner-friendly.

## Episode 1 Scope

Episode 1 is called **"Building Avi: First Flight with pyATS SSH"**.

The goal is simple:

- Connect to one Cisco IOS-XE lab device using pyATS and Unicon over SSH.
- Run one read-only command: `show ip interface brief`.
- Return a basic report.
- Log the tool call.

## Important Rules

- Do not add configuration-changing code in Episode 1.
- Do not include `conf t`.
- Do not include configuration commands.
- Do not configure devices.
- Do not use Netmiko in Episode 1.
- Prefer pyATS for network connectivity in Episode 1.
- Keep real credentials out of committed files.
- Commit only `testbed.example.yaml`; the real `testbed.yaml` must stay ignored.

## Style Guidance

- Preserve beginner-friendly comments.
- Keep code readable and educational.
- Avoid clever abstractions unless they clearly help the lesson.
- Use a conversational, practical tone in markdown.
- Write for network engineers learning agentic automation.
- Use the Avi metaphor lightly: pilot, first flight, instrument, black box recorder.

Episode 1 should be camera-ready and easy to explain line by line.
