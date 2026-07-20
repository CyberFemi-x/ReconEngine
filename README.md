<<<<<<< HEAD
# Recon Engine
## Local Lab Information

The local lab was successfully initialized and generated a runtime configuration for this development environment.

Current authorized services:

- HTTP Discovery Service: `127.0.0.1:18090`
- Line Protocol Discovery Service: `127.0.0.1:22537`

Runtime configuration:

- Bind Address: `127.0.0.1`
- Entry URL: `http://127.0.0.1:18090/`
- Maximum Request Rate: **25 requests/second**
- Request Budget: **240 requests**

The generated `scope.csv` currently authorizes:

| Target | Status | Purpose |
|---------|--------|---------|
| 127.0.0.1:18090 | IN | HTTP discovery target |
| 127.0.0.1:22537 | IN | Line-protocol discovery target |
| 127.0.0.1:27062 | OUT | Scope validation test (must never be contacted) |
| 0.0.0.0/0 | OUT | All non-loopback destinations are prohibited |

The Recon Engine will load these values dynamically during execution rather than using hard-coded configuration.

## Overview

Recon Engine is a Python-based reconnaissance tool being developed as part of the UBI Advanced Programme – Ethical Hacking/VAPT Stage 5 assessment.

The goal of the project is to perform safe and controlled reconnaissance against the supplied local laboratory environment while strictly enforcing the assessment rules of engagement. The engine will collect, normalize, and report discovery information without performing unauthorized exploitation.

## Project Objectives

The Recon Engine is being designed to:

* Validate targets against the provided scope before any network communication.
* Perform safe reconnaissance within the authorized local lab.
* Normalize discovery results into a common format.
* Preserve raw tool output for evidence.
* Generate structured reports.
* Support resumable scans.
* Enforce request rate and request budget limits.

## Current Project Status

The project has been initialized.

Current progress includes:

* Python virtual environment created.
* Git repository initialized.
* Initial project directory structure created.
* Assessment archive verified using its SHA-256 hash before extraction.
* Local assessment lab extracted.
* Local lab started using the assigned marker.
* Runtime configuration generated successfully.
* Initial review of the generated `assignment.json` and `scope.csv` completed.

No reconnaissance functionality has been implemented yet.

## Project Structure

```text
ReconEngine/
│
├── recon_engine/
├── tests/
├── schemas/
├── raw-output/
├── README.md
├── .gitignore
└── venv/
```

## Local Lab Information

The local lab generates runtime configuration files including:

* `assignment.json`
* `scope.csv`

These files define:

* Authorized targets
* Authorized ports
* Request rate limits
* Request budget
* Runtime identifiers

The engine will use these files during execution instead of hard-coded values.

## Development Notes

Development follows an incremental approach.

Each feature will be implemented, tested, and committed separately to maintain a clear and reproducible Git history.

## Current Stage

Project initialization complete.

Next milestone:

* Build the command-line interface (CLI).
* Implement configuration loading.
* Implement scope validation.
=======
# ReconEngine
A modular Python reconnaissance engine with scope validation, evidence collection, and normalized reporting for authorized security assessments.
>>>>>>> 8f49c85f1074a898f983aff0a7a505022bded17c
