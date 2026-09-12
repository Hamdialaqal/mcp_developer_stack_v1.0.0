#!/usr/bin/env python3
"""
Starter Autonomous Agent Loop (Zero External Dependencies)
"""
import os
import json

class StarterAgent:
    def __init__(self, agent_name: str, tools_file: str = ""):
        self.agent_name = agent_name
        if not tools_file or not os.path.exists(tools_file):
            base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            tools_file = os.path.join(base, "dataset", "mcp_servers_free.json")
        with open(tools_file, 'r', encoding='utf-8') as f:
            self.tools = json.load(f)
            
    def decide_next_step(self, user_goal: str) -> str:
        goal_lower = user_goal.lower()
        if "search" in goal_lower or "web" in goal_lower:
            return "mcp-free-02"  # Brave Search
        elif "sql" in goal_lower or "database" in goal_lower:
            return "mcp-free-01"  # SQLite
        elif "git" in goal_lower or "code" in goal_lower:
            return "mcp-free-04"  # Git
        return "mcp-free-05"       # Memory default

    def run_goal(self, goal: str):
        print(f"[{self.agent_name}] Evaluating Goal: '{goal}'")
        selected_tool_id = self.decide_next_step(goal)
        tool_meta = next(t for t in self.tools if t["id"] == selected_tool_id)
        print(f"[{self.agent_name}] Selected Tool: {tool_meta['name']} (ID: {selected_tool_id})")
        print(f"[{self.agent_name}] Ready to invoke MCP endpoint: {tool_meta['protocol']}")
        return {"goal": goal, "tool_assigned": tool_meta["name"], "status": "READY"}

if __name__ == "__main__":
    agent = StarterAgent("FreeStarterAgent")
    agent.run_goal("Find recent papers on LLM agents on the web")
