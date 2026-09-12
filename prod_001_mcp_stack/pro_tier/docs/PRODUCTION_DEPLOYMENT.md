# Production Deployment Manual

## 1. Local Development
Run the containerized stack:
```bash
docker compose -f pro_tier/mcp/docker-compose.mcp-servers.yml up -d
```

## 2. Production VPS Setup (Ubuntu 22.04 / 24.04)
1. Install Docker and Docker Compose plugin.
2. Clone repository into `/opt/mcp-stack`.
3. Set environment variables in `.env`.
4. Use Systemd to supervise persistent agent workers.

## 3. Monitoring & Telemetry
Log all tool invocations with execution timestamps, input payloads, return statuses, and token latencies.
