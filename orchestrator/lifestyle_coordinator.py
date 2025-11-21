from agents.task_priority_agent import TaskPriorityAgent
from agents.habit_coach_agent import HabitCoachAgent
from agents.productivity_insights_agent import ProductivityInsightsAgent
from agents.goal_escalation_agent import GoalEscalationAgent
from tools.task_database import TaskDatabase
from tools.productivity_tracker import ProductivityTracker
from tools.reflection_logger import ReflectionLogger
from memory.session_memory import SessionMemory
from memory.long_term_memory import LongTermMemory

class LifestyleCoordinator:
    def __init__(self):
        self.task_db = TaskDatabase()
        self.tracker = ProductivityTracker()
        self.reflection_logger = ReflectionLogger()
        self.session_memory = SessionMemory()
        self.long_term_memory = LongTermMemory()

        self.task_agent = TaskPriorityAgent(self.task_db)
        self.habit_agent = HabitCoachAgent(self.tracker, self.reflection_logger)
        self.insight_agent = ProductivityInsightsAgent(
            self.task_db, self.tracker, self.reflection_logger
        )
        self.goal_agent = GoalEscalationAgent()

    def _route(self, message):
        m = message.lower()

        if any(w in m for w in ["task", "todo", "deadline"]):
            return "task"
        if any(w in m for w in ["habit", "routine", "study", "focus"]):
            return "habit"
        if any(w in m for w in ["goal", "stuck", "where to start"]):
            return "goal"

        return "insight"

    def handle_message(self, user_id, message):
        self.session_memory.add_message(user_id, "user", message)

        profile = self.long_term_memory.get_user_profile(user_id)
        context = {
            "user_id": user_id,
            "user_profile": profile,
            "recent_messages": self.session_memory.messages.get(user_id, [])
        }

        route = self._route(message)

        if route == "task":
            return self.task_agent.process(message, context)
        if route == "habit":
            return self.habit_agent.process(message, context)
        if route == "goal":
            return self.goal_agent.process(message, context)

        return self.insight_agent.process(message, context)
