class ReflectionLogger:
    def __init__(self):
        self.logs = []

    def log_reflection(self, user_id, text):
        self.logs.append({"user_id": user_id, "text": text})
