"""
Minimal Standalone Hierarchical Supervisor Demo
Demonstrates deterministic state routing across 3 specialized agent workers.
"""

from typing import List, Dict, Any

class SimpleAgentState:
    def __init__(self, task: str):
        self.task = task
        self.history: List[Dict[str, str]] = []
        self.completed = False

def supervisor(state: SimpleAgentState) -> str:
    senders = [m["sender"] for m in state.history]
    if "researcher" not in senders:
        return "researcher"
    elif "coder" not in senders:
        return "coder"
    elif "reviewer" not in senders:
        return "reviewer"
    return "FINISH"

def worker_researcher(state: SimpleAgentState):
    print("🔍 [Researcher]: Analyzing architectural boundaries for task...")
    state.history.append({"sender": "researcher", "content": "Verified type requirements and edge cases."})

def worker_coder(state: SimpleAgentState):
    print("💻 [Coder]: Implementing type-safe Python solution...")
    state.history.append({"sender": "coder", "content": "class Solution: def run(self): return True"})

def worker_reviewer(state: SimpleAgentState):
    print("🛡️ [Reviewer]: Running security audit & OWASP sanity check...")
    state.history.append({"sender": "reviewer", "content": "All boundary checks pass. 0 vulnerabilities."})

def main():
    state = SimpleAgentState(task="Build resilient rate-limiting middleware")
    print(f"🚀 Initializing Multi-Agent System for task: '{state.task}'\n")

    while not state.completed:
        next_step = supervisor(state)
        print(f"👑 Supervisor dispatch -> {next_step}")
        if next_step == "researcher":
            worker_researcher(state)
        elif next_step == "coder":
            worker_coder(state)
        elif next_step == "reviewer":
            worker_reviewer(state)
        elif next_step == "FINISH":
            state.completed = True
            print("\n✅ Multi-agent execution finished successfully!")

if __name__ == "__main__":
    main()
