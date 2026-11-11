# Apex AI Quality Engineering

A portfolio project for evaluating AI applications in a simulated financial-services environment.

## Project goals
- Build a financial-support chatbot backed by a small, versioned knowledge base.
- Create a golden dataset with expected facts and evaluation criteria.
- Add deterministic and model-assisted evaluators.
- Test RAG retrieval, hallucinations, prompt injection, PII handling, and MCP tool use.
- Compare evaluation runs and enforce CI release gates.

## Current status
Day 1 scaffold. No live LLM integration or real trading functionality is included yet.

## Setup (macOS + VS Code)

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

In VS Code, open this folder and select the interpreter at `.venv/bin/python`.

## Run the starter tests

```bash
python -m pytest -q
```

## Safety
This is an educational simulation. Never connect it to a real exchange account, API key, wallet, or order endpoint.
