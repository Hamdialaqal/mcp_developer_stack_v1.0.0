# MCP Developer Stack: System Architecture

## 1. Principles
The Model Context Protocol (MCP) decouples LLM reasoning engines from operational tool execution.
Instead of binding tools directly into model prompt weights, the architecture follows an **RPC Client-Server Paradigm**:
- **Client (Host Application)**: The Agent runtime (e.g. Spark, Claude, Cursor, Custom FastAPI).
- **Protocol**: JSON-RPC 2.0 over Stdio (local) or Server-Sent Events / SSE (remote).
- **Server (Tool Provider)**: Sandboxed lightweight process exposing tools, prompts, and resources.

## 2. Component Diagram
```text
┌──────────────────────────────┐
│     Agent Reasoning Core     │
│   (LLM + Supervisor Loop)    │
└──────────────┬───────────────┘
               │ JSON-RPC 2.0
               ▼
┌──────────────────────────────┐
│    Intelligent Tool Router   │
│   (Schema Validation & RAG)  │
└──────┬───────────────┬───────┘
       ▼               ▼
┌──────────────┐ ┌──────────────┐
│  Local MCPs  │ │  Remote MCPs │
│ (DB/File/Git)│ │(Stripe/Search│
└──────────────┘ └──────────────┘
```

## 3. Reliability Safeguards
- **Timeout Isolation**: Each MCP call must be bounded by an explicit timeout (default: 15s).
- **Mutating Action Quarantine**: Operations modifying live data require strict logging and transactional rollback blocks.
