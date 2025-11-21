import json
from typing import Dict, Any
from agents.base_agent import BaseAgent

class TaskPriorityAgent(BaseAgent):
    """
    Classifies tasks into priority levels and stores them in the task DB.
    """

    def __init__(self, task_db, model=None):
        super().__init__(model=model)
        self.task_db = task_db

    def process(self, message: str, context: Dict[str, Any]):
        prompt = f"""
You are a productivity assistant. The user will describe tasks.

Your role:
1. Extract tasks.
2. Assign priority: urgent, high, medium, low.
3. Give a brief next action.

Block medical/legal/financial topics.

Respond ONLY in JSON:
{{
  "tasks": [
    {{
      "description": "string",
      "priority": "urgent|high|medium|low|unsupported",
      "next_action": "string"
    }}
  ]
}}
"""
        raw = self._call_model(prompt)
        parsed = self._json_from_response(raw)

        if not parsed:
            task = self.task_db.add_task(context["user_id"], message)
            self.task_db.update_task_priority(task.id, "medium")
            return {
                "agent": "task_priority",
                "tasks": [
                    {
                        "description": message,
                        "priority": "medium",
                        "next_action": "Focus 25 minutes.",
                        "task_id": task.id
                    }
                ],
                "note": "LLM fallback"
            }

        results = []
        for t in parsed["tasks"]:
            task = self.task_db.add_task(context["user_id"], t["description"])
            self.task_db.update_task_priority(task.id, t["priority"])
            results.append({
                "description": t["description"],
                "priority": t["priority"],
                "next_action": t["next_action"],
                "task_id": task.id
            })

        return {"agent": "task_priority", "tasks": results}
