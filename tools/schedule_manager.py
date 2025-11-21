class ScheduleManager:
    def __init__(self):
        self.entries = []

    def add_block(self, user_id, title, start, end):
        self.entries.append({
            "user_id": user_id,
            "title": title,
            "start": start,
            "end": end
        })
