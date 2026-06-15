# AI Usage

## Tools Used

- ChatGPT
- VS Code Copilot (if used)

## Example Prompts

1. Design PostgreSQL schema for shared expense application.
2. Create Django models for memberships and transactions.

## AI Mistake 1

Issue:
Suggested storing CSV contents inside a Python file.

Detection:
Import errors occurred.

Fix:
Separated CSV data from service files.

## AI Mistake 2

Issue:
Suggested duplicate detection logic before verifying service integration.

Detection:
Anomalies key was missing.

Fix:
Verified CSV import flow first.

## AI Mistake 3

Issue:
Incorrect module import path during testing.

Detection:
ModuleNotFoundError raised.

Fix:
Corrected file names and package structure.
