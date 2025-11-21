import json
from typing import Dict, Any
from agents.base_agent import BaseAgent

class HabitCoachAgent(BaseAgent):
    def __init__(self, tracker, reflection_logger, model=None):
        super().__init__(model=model)
        self.tracker = tracker
        self.reflection_logger = reflection_logger

    def process(self, message: str, context: Dict[str, Any]):
        prompt = f"""
You are a productivity habit coach.
Scope: study routines, time mgmt, focus, habits.
DO NOT give medical/legal/financial advice.

Respond ONLY in:
{{
  "tips": ["..."],
  "encouragement": "string",
  "notes": "string"
}}
"""
        raw = self._call_model(prompt)
        parsed = self._json_from_response(raw)

        if not parsed:
            parsed = {
                "tips": [
                    "Write top 3 tasks.",
                    "Use 25-minute focus timer.",
                    "Avoid distractions for 1 session."
                ],
                "encouragement": "Small steps matter!",
                "notes": "Fallback"
            }

        self.reflection_logger.log_reflection(
            context["user_id"],
            f"User: {message} | Coach: {parsed['encouragement']}"
        )

        parsed["agent"] = "habit_coach"
        return parsed
