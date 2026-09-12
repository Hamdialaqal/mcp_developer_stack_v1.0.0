#!/usr/bin/env python3
"""
Minimal MCP Tool Runner (Standard Library Python)
Demonstrates dispatching a structured JSON-RPC call to an MCP-compliant tool schema.
"""
import os
import json

class MockMCPClient:
    def __init__(self, catalog_path: str):
        if not os.path.isabs(catalog_path):
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            catalog_path = os.path.join(base, "dataset", "mcp_servers_free.json")
        with open(catalog_path, 'r', encoding='utf-8') as f:
            self.catalog = json.load(f)
            
    def list_available_tools(self):
        return [
            {"id": s["id"], "name": s["name"], "category": s["category"]}
            for s in self.catalog
        ]
        
    def execute_tool_call(self, tool_id: str, arguments: dict) -> dict:
        matched = next((s for s in self.catalog if s["id"] == tool_id), None)
        if not matched:
            return {"status": "error", "message": f"Tool {tool_id} not found in catalog"}
            
        return {
            "status": "success",
            "executed_tool": matched["name"],
            "protocol": matched["protocol"],
            "received_args": arguments,
            "mock_result": f"Simulated output from {matched['name']}"
        }

if __name__ == "__main__":
    client = MockMCPClient("")
    print("[*] Available Free MCP Tools:")
    for tool in client.list_available_tools():
        print(f"  - [{tool['id']}] {tool['name']} ({tool['category']})")
        
    print("\n[*] Dispatching test execution to SQLite MCP:")
    res = client.execute_tool_call("mcp-free-01", {"query": "SELECT COUNT(*) FROM users;"})
    print(json.dumps(res, indent=2))
