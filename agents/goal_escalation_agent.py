import json
from typing import Dict, Any
from agents.base_agent import BaseAgent

class GoalEscalationAgent(BaseAgent):
    def process(self, message: str, context: Dict[str, Any]):
        prompt = """
Break big goals into smaller steps.
Respond ONLY JSON:
{
  "goal_clarified": "...",
  "steps": ["...", "..."],
  "encouragement": "..."
}
"""
        raw = self._call_model(prompt)
        parsed = self._json_from_response(raw)

        if not parsed:
            parsed = {
                "goal_clarified": message,
                "steps": [
                    "Write a clear end-goal.",
                    "List sub-tasks.",
                    "Start the first task for 20 mins."
                ],
                "encouragement": "You can do this!"
            }

        parsed["agent"] = "goal_escalation"
        return parsed
