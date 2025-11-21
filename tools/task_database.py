from dataclasses import dataclass, field
import datetime as dt
import uuid

@dataclass
class Task:
    id: str
    user_id: str
    description: str
    priority: str = "unknown"
    status: str = "pending"
    created_at: dt.datetime = field(default_factory=dt.datetime.utcnow)

class TaskDatabase:
    def __init__(self):
        self.tasks = {}

    def add_task(self, user_id, description):
        tid = str(uuid.uuid4())
        t = Task(id=tid, user_id=user_id, description=description)
        self.tasks[tid] = t
        return t

    def list_tasks_for_user(self, user_id):
        return [t for t in self.tasks.values() if t.user_id == user_id]

    def update_task_priority(self, task_id, priority):
        self.tasks[task_id].priority = priority
