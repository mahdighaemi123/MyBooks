# quest_model.py
# This file contains the "blueprint" for our quests.
# We import the datetime magic (from Chapter 14).
import datetime


class Quest:
    """
    Blueprint for a single quest in our Quest Log.
    Uses magic from Chapter 12 (Classes).
    """

    def __init__(self, title, description):
        # 1. Attributes from the user
        self.title = title
        self.description = description

        # 2. Automatic attributes (Chapter 14 magic)
        self.created_at = datetime.datetime.now()

        # 3. Default status
        self.status = "Pending"  # Other status: "Complete"

    def display_info(self):
        """
        Prints the details of this quest in a neat format.
        Uses magic from Chapter 14 (strftime) and Chapter 10 (f-strings).
        """
        # Format the date into a readable string
        date_str = self.created_at.strftime("%Y-%m-%d %H:%M")

        print(f"  Title: {self.title}")
        print(f"  Status: {self.status}")
        print(f"  Created: {date_str}")
        print(f"  Description: {self.description}")

    def complete_quest(self):
        """
        Changes the status of the quest to "Complete".
        """
        self.status = "Complete"
        print(f"\n[Quest '{self.title}' marked as complete!]")
