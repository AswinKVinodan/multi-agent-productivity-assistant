import json
from typing import Dict, Any
from agents.base_agent import BaseAgent

class ProductivityInsightsAgent(BaseAgent):
    def __init__(self, task_db, tracker, reflection_logger, model=None):
        super().__init__(model=model)
        self.task_db = task_db
        self.tracker = tracker
        self.reflection_logger = reflection_logger

    def process(self, message: str, context: Dict[str, Any]):
        tasks = [
            {"description": t.description, "priority": t.priority, "status": t.status}
            for t in self.task_db.list_tasks_for_user(context["user_id"])
        ]

        total_focus = self.tracker.total_focus_time_for_user(context["user_id"])

        prompt = f"""
You analyze user productivity patterns.
Scope: planning, task mgmt, workflow improvement.

Respond ONLY in:
{{
  "action": "analysis|general",
  "summary": "string",
  "suggestions": ["..."],
  "caveats": "string"
}}
"""
        raw = self._call_model(prompt)
        parsed = self._json_from_response(raw)

        if not parsed:
            parsed = {
                "action": "general",
                "summary": "You may have many tasks competing.",
                "suggestions": [
                    "Work on 1 task for the next 25 mins.",
                    "Reduce daily list to 3 items.",
                    "Track progress daily."
                ],
                "caveats": "General advice only."
            }

        parsed["agent"] = "productivity_insights"
        return parsed