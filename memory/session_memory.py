class SessionMemory:
    def __init__(self, max_messages=10):
        self.max = max_messages
        self.messages = {}

    def add_message(self, user_id, role, content):
        self.messages.setdefault(user_id, [])
        self.messages[user_id].append({"role": role, "content": content})
        if len(self.messages[user_id]) > self.max:
            self.messages[user_id] = self.messages[user_id][-self.max:]
