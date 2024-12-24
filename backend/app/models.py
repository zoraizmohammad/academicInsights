class Activity:
    def __init__(self, user_id, activity, timestamp):
        self.user_id = user_id
        self.activity = activity
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "activity": self.activity,
            "timestamp": self.timestamp
        }
