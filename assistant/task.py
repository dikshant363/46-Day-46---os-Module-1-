import datetime

class Task:
    def __init__(self, title, category="Personal", priority="Medium", due_date=None, reminders=None, recurrence="none", completed=False):
        self.title = title
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.reminders = reminders if reminders is not None else []
        self.recurrence = recurrence
        self.completed = completed
        self.created_at = datetime.datetime.now()

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority}, Category: {self.category})"

    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "reminders": self.reminders,
            "recurrence": self.recurrence,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        due_date = datetime.datetime.fromisoformat(data["due_date"]) if data["due_date"] else None
        task = cls(
            title=data["title"],
            category=data["category"],
            priority=data["priority"],
            due_date=due_date,
            reminders=data["reminders"],
            recurrence=data["recurrence"],
            completed=data["completed"]
        )
        task.created_at = datetime.datetime.fromisoformat(data["created_at"])
        return task
