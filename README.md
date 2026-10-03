# 🚀 Awesome LangGraph Multi-Agent Production Starter Kit (2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-brightgreen.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Production%20Ready-orange.svg)](https://github.com/langchain-ai/langgraph)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)

> Production-ready hierarchical multi-agent orchestration architecture built with **LangGraph**, **FastAPI**, **Pydantic v2**, and **Docker**. Deploy autonomous supervisor-worker pipelines in under 15 minutes.

---

### 🎁 Need the Full Enterprise Distribution?
> Get the complete enterprise repository with **PostgreSQL Checkpointer State Persistence**, **Real-Time WebRTC Voice Interface**, and **Docker Compose Production Stack**:  
> 👉 **[Download Full Production Bundle on Gumroad (50% OFF with code LAUNCH50)](https://masbintoro.gumroad.com/l/langgraph-multi-agent-starter-kit/LAUNCH50)**

---

## 🏛️ Architectural Overview

```text
                     ┌───────────────────────────┐
                     │   User Request / Webhook  │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │    Supervisor Agent 🧠    │
                     │  (Router & Task Assigner) │
                     └──────┬──────┬──────┬──────┘
                            │      │      │
            ┌───────────────┘      │      └──────────────┐
            ▼                      ▼                     ▼
┌──────────────────────┐ ┌───────────────────┐ ┌───────────────────┐
│   Researcher Agent   │ │    Coder Agent    │ │   Reviewer Agent  │
│ (Tavily/Exa Search)  │ │ (Code Synthesizer)│ │(Static & Security)│
└───────────┬──────────┘ └─────────┬─────────┘ └─────────┬─────────┘
            │                      │                     │
            └──────────────────────┼─────────────────────┘
                                   │
                                   ▼
                     ┌───────────────────────────┐
                     │    Synthesized Output     │
                     │  & State Memory Checkpoint│
                     └───────────────────────────┘
```

## ✨ Core Features
- **Hierarchical Supervisor Pattern**: Autonomous task routing between specialized sub-agents with dynamic course correction.
- **SSE Real-Time Streaming**: Stream intermediate LLM tokens and execution traces via FastAPI Server-Sent Events.
- **Strict Pydantic v2 Schemas**: Zero runtime hallucinations with strongly-typed structured JSON inputs and outputs.
- **Pluggable LLM Providers**: 1-click model switching between Claude 3.7 Sonnet, OpenAI GPT-4o, and DeepSeek-R1.

## ⚡ Quickstart (60 Seconds)

```bash
# Clone the repository
git clone https://github.com/jarumgoni/awesome-langgraph-multi-agent-starter.git
cd awesome-langgraph-multi-agent-starter

# Run standalone demo
python3 supervisor_demo.py
```

## 📄 License
MIT License. Created & maintained by [Masbin / ProChat Commerce Labs](https://prochatcommerce.com).
