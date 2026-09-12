# MCP & Autonomous Agent Developer Stack (2026 Edition)
> Production-ready Model Context Protocol (MCP) schemas, curated tool catalogs, and plug-and-play Python agent blueprints.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Production MVP](https://img.shields.io/badge/Status-Validated%20MVP-success.svg)]()
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)]()

## Overview
Building reliable autonomous agents in 2026 requires more than raw prompt engineering. As LLM tool calling migrates to the **Model Context Protocol (MCP)**, engineering teams face fragmented documentation, unvetted community scripts, and missing machine-readable catalogs.

This repository provides **vetted, production-tested MCP server catalogs, structured JSON/CSV datasets, and zero-dependency Python agent workflows** to reduce initial configuration time for standard MCP servers.

---

## Tiers & Package Structure

| Feature | FREE Community Tier | PRO Developer Tier |
| :--- | :--- | :--- |
| **Curated MCP Servers** | 5 Core Servers | 25+ Production Servers |
| **Formats Provided** | JSON & CSV | JSON, CSV, Pydantic Models, Docker Compose |
| **Agent Blueprints** | Single-tool CLI Runner | Multi-Agent Supervisor & Resilient Runner |
| **Cost & Latency Benchmarks** | Basic | Exhaustive with Enterprise Pricing Matrix |
| **Ready-to-use Workflows** | 1 Starter Workflow | 5 End-to-End Enterprise Workflows |
| **License** | MIT (Open Source) | Commercial Developer License |

---

## Directory Layout
```text
prod_001_mcp_stack/
├── free_tier/
│   ├── dataset/
│   │   ├── mcp_servers_free.json
│   │   └── mcp_servers_free.csv
│   ├── examples/
│   │   └── minimal_mcp_client.py
│   └── templates/
│       └── starter_agent.py
├── pro_tier/
│   ├── dataset/
│   │   ├── mcp_servers_pro.json
│   │   ├── mcp_servers_pro.csv
│   │   └── mcp_benchmark_matrix.json
│   ├── mcp/
│   │   ├── docker-compose.mcp-servers.yml
│   │   └── server_configs.json
│   ├── agents/
│   │   ├── autonomous_supervisor.py
│   │   └── tool_router.py
│   ├── templates/
│   │   ├── research_agent_workflow.py
│   │   ├── code_review_pipeline.py
│   │   └── financial_audit_agent.py
│   └── docs/
│       ├── ARCHITECTURE.md
│       ├── SECURITY_AND_AUTH.md
│       └── PRODUCTION_DEPLOYMENT.md
├── sales_page/
│   └── index.html
├── LICENSE
└── CHANGELOG.md
```

---

## Quick Start (Free Tier)

### 1. Inspect the Dataset
```bash
python3 -c "import json; data = json.load(open('free_tier/dataset/mcp_servers_free.json')); print(f'Loaded {len(data)} vetted MCP servers')"
```

### 2. Run the Minimal Agent
```bash
python3 free_tier/examples/minimal_mcp_client.py
```

---

## Why Developers Choose This Stack
1. **Machine-Readable Precision**: Every MCP entry specifies exact schema inputs, authentication protocols, cost models, and rate limits.
2. **Zero Halting Bugs**: Tested against Python 3.10+ with standard library / zero bloated dependencies.
3. **Enterprise Defense**: Clear separation between read-only tools and mutating side-effects.

---

## Support & Contributions
For issues, contributions, or commercial team licensing, consult [docs/ARCHITECTURE.md](pro_tier/docs/ARCHITECTURE.md).
