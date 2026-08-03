# In quest_model.py
import datetime


class Quest:
    def __init__(self, title, description, deadline="None", priority="Normal"):
        self.title = title
        self.description = description
        self.status = "Pending"
        self.created_at = datetime.datetime.now()

        # --- NEW ATTRIBUTES ---
        self.deadline = deadline
        self.priority = priority

    def display_info(self):
        # Add icon for High Priority
        icon = "⭐" if self.priority == "High" else "🔹"

        print(f"{icon} Title: {self.title}")
        print(f"   Priority: {self.priority}")
        print(f"   Deadline: {self.deadline}")
        print(f"   Status: {self.status}")

    def complete_quest(self):
        """
        Changes the status of the quest to "Complete".
        """
        self.status = "Complete"
        print(f"\n[Quest '{self.title}' marked as complete!]")
