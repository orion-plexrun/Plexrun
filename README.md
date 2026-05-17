# PlexRun Python SDK

> The orchestration runtime for AI workflows.

## Install

pip install plexrun  (coming soon — private beta)

## Quickstart

```python
from plexrun import workflow, step

@workflow
def research_pipeline(topic: str):
    draft = summarize(topic)
    return write_report(draft)

@step(model="gpt-4o", retries=3)
def summarize(topic: str) -> str:
    ...

@step(model="gpt-4o")
def write_report(draft: str) -> str:
    ...
## Features
 
- **DAG-based execution** — Define step dependencies, fan-out, fan-in
- **Idempotent retries** — Failed steps retry without duplicate LLM calls  
- **Per-step traces** — Token usage, cost, and latency for every step
- **Serverless workers** — No fleet to manage, auto-scales with queue depth
- **YAML workflows** — Declarative pipeline definitions supported
 
## CLI
 
```bash
# Install CLI
pip install plexrun
 
# Initialize a new project
plexrun init my-pipeline
 
# Deploy workflow
plexrun deploy workflow.py
 
# Trigger a run
plexrun run research_pipeline --input '{"topic": "AI in healthcare"}'
 
# View live logs
plexrun logs <run-id>

## Status

| Component      | Status      |
|----------------|-------------|
| Python SDK     | Alpha       |
| CLI            | Alpha       |
| TypeScript SDK | In progress |
| Dashboard      | In progress |

Currently in private beta. [Join the waitlist →](https://plexrun.com/#waitlist)

Links
Website: plexrun.com
Docs: plexrun.com/docs/quickstart
Contact: hello@plexrun.com
