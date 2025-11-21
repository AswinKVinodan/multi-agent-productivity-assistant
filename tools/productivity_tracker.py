class ProductivityTracker:
    def __init__(self):
        self.sessions = []

    def log_focus_session(self, user_id, minutes, task_id=None):
        self.sessions.append({
            "user_id": user_id,
            "task_id": task_id,
            "minutes": minutes
        })

    def total_focus_time_for_user(self, user_id):
        return sum(s["minutes"] for s in self.sessions if s["user_id"] == user_id)
