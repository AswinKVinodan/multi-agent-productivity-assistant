import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from orchestrator.lifestyle_coordinator import LifestyleCoordinator

assistant = LifestyleCoordinator()

def format_result(result):
    agent = result.get("agent")
    out = f"[{agent.upper()}]\n"
    for k, v in result.items():
        if k != "agent":
            out += f"- {k}: {v}\n"
    return out

def main():
    print("=== Multi-Agent Productivity Assistant ===")
    print("Type 'exit' to quit.\n")

    user_id = "demo"

    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            break

        result = assistant.handle_message(user_id, msg)
        print(format_result(result))

if __name__ == "__main__":
    main()
