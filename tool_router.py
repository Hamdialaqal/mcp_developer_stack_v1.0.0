#!/usr/bin/env python3
"""
Intelligent Tool Router (Pro Tier)
Matches user intentions to exact MCP servers and parameter schemas.
"""
import os
import json

class ToolRouter:
    def __init__(self, catalog_path: str = ""):
        if not catalog_path or not os.path.exists(catalog_path):
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            catalog_path = os.path.join(base, "dataset", "mcp_servers_pro.json")
        with open(catalog_path, 'r', encoding='utf-8') as f:
            self.tools = json.load(f)

    def route_query(self, query: str) -> dict:
        q = query.lower()
        if any(w in q for w in ["database", "sql", "postgres", "table"]):
            return self._match("mcp-pro-01")
        elif any(w in q for w in ["search", "web", "find on internet", "google"]):
            return self._match("mcp-pro-06")
        elif any(w in q for w in ["scrape", "crawl", "html", "extract website"]):
            return self._match("mcp-pro-09")
        elif any(w in q for w in ["pdf", "invoice", "document", "generate report"]):
            return self._match("mcp-pro-20")
        elif any(w in q for w in ["email", "notify", "send message"]):
            return self._match("mcp-pro-18")
        elif any(w in q for w in ["billing", "stripe", "payment", "charge"]):
            return self._match("mcp-pro-16")
        return self._match("mcp-pro-13")

    def _match(self, tool_id: str) -> dict:
        matched = next((t for t in self.tools if t["id"] == tool_id), None)
        return {
            "assigned_tool_id": tool_id,
            "tool_name": matched["name"] if matched else "Unknown",
            "category": matched["category"] if matched else "General",
            "cost_model": matched["cost_model"] if matched else "N/A"
        }

if __name__ == "__main__":
    router = ToolRouter()
    queries = [
        "Generate a PDF customer statement",
        "Search the web for competitor pricing updates",
        "Query the PostgreSQL database for revenue this week",
        "Charge customer via Stripe subscription"
    ]
    for q in queries:
        print(f"Query: '{q}' -> Matched: {router.route_query(q)}")
