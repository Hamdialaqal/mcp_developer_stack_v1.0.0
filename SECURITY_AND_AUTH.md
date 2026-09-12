# Security, Sandboxing, and Authentication Guide

## 1. Zero Trust Secret Management
- Never hardcode API keys or secrets in prompt texts, logs, or code repositories.
- Use environment variables (`.env`) or a secrets manager like HashiCorp Vault / Infisical.

## 2. Defense Against Indirect Prompt Injection
When an agent scrapes third-party web content via MCP, hostile instructions may be embedded in raw HTML.
- **Remediation**:
  - Always clean and verbalize scraped text before placing it into the agent's context.
  - Never allow tools that read unverified input to directly trigger mutating actions (e.g., executing bash commands or sending financial transactions) without strict boundary enforcement.

## 3. Sandboxed Execution
Run untrusted code or arbitrary scrapers inside isolated Docker containers with non-root privileges and no host filesystem mounts.
