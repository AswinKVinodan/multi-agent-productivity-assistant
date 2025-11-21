class LongTermMemory:
    def __init__(self):
        self.profiles = {}

    def get_user_profile(self, user_id):
        return self.profiles.setdefault(user_id, {"goals": [], "notes": ""})

    def update_user_profile(self, user_id, updates):
        self.profiles[user_id].update(updates)
