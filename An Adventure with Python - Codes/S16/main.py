# main.py
# This is our main command center.

# --- 1. SUMMONING OUR MAGIC ---
import json                   # For eternal memory (Chapter 11)
import datetime               # For time magic (Chapter 14)
from quest_model import Quest  # Our own blueprint! (Chapter 13)

# Global variables (our magic scrolls)
quest_list = []  # This is our main "backpack" for quests
SAVE_FILE = "quest_log.json"  # The name of our eternal memory file"


# --- 2. ETERNAL MEMORY SPELLS (Chapter 11 Magic) ---

def load_quests():
    """
    Loads the quest list from the JSON file at the start.
    Uses try...except to handle the first run.
    """
    global quest_list
    try:
        with open(SAVE_FILE, "r") as f:
            # 1. Load the simple data (list of dictionaries)
            data_list = json.load(f)

            # 2. Re-create the Quest objects
            quest_list = []  # Clear the list before loading
            for item in data_list:
                # Create a new quest object
                quest = Quest(item['title'], item['description'])
                # Restore its saved data
                quest.status = item['status']
                quest.created_at = datetime.datetime.fromisoformat(
                    item['created_at'])
                quest_list.append(quest)

        print(f"Quest Log loaded. {len(quest_list)} quests found.")
    except FileNotFoundError:
        print("No save file found. Starting a new Quest Log.")
    except Exception as e:
        print(f"An error occurred while loading: {e}")


def save_quests():
    """
    Saves the current quest_list to the JSON file before quitting.
    """
    # 1. We must convert our list of Objects into a list of Dictionaries
    data_list = []
    for quest in quest_list:
        # Convert datetime object to a string to save in JSON
        date_str = quest.created_at.isoformat()

        data_list.append({
            "title": quest.title,
            "description": quest.description,
            "created_at": date_str,
            "status": quest.status
        })

    # 2. Now, save the simple list of dictionaries
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(data_list, f, indent=4)
        print("Quests saved successfully!")
    except Exception as e:
        print(f"An error occurred while saving: {e}")


# --- 3. INTERACTIVE SPELLS (Chapter 8 Magic) ---

def add_quest():
    """
    Asks the user for quest details and adds a new Quest to the list.
    """
    print("\n--- Add New Quest ---")
    title = input("Enter quest title: ")
    description = input("Enter quest description: ")

    # Create a new Quest object (using our blueprint)
    new_quest = Quest(title, description)

    # Add it to our main backpack
    quest_list.append(new_quest)
    print("\n[Quest added successfully!]")


def show_all_quests():
    """
    Displays all quests in the quest_list.
    Uses magic from Chapter 15 (enumerate) and Chapter 12 (methods).
    """
    print("\n--- Your Current Quest Log ---")
    if not quest_list:
        print("Your quest log is empty. Time to find adventure!")
        return

    # Use 'enumerate' to get a clean index (Chapter 15 magic)
    for index, quest in enumerate(quest_list):
        print(f"\n--- Quest {index + 1} ---")
        quest.display_info()  # Call the method from our class!
        print("--------------------")


def complete_quest():
    """
    Asks the user which quest to mark as complete.
    """
    # Show them the list first
    show_all_quests()
    if not quest_list:
        return  # Nothing to complete

    try:
        choice = input("Enter the number of the quest to complete: ")
        # Convert choice to a zero-based index
        index = int(choice) - 1

        # Check if the index is valid
        if 0 <= index < len(quest_list):
            quest_list[index].complete_quest()
        else:
            print("Invalid quest number! No quest was completed.")

    except ValueError:
        print("That's not a number! Spell failed.")


# --- 4. THE MAIN SPELL LOOP (Chapter 4 Magic) ---

def main():
    """
    The main entry point of our program.
    """
    # Load quests from our eternal memory first!
    load_quests()

    while True:
        print("\n===== Adventurer's Quest Log =====")
        print("1. Add a new quest")
        print("2. Show all quests")
        print("3. Complete a quest")
        print("4. Save and Quit")
        print("====================================")
        choice = input("Cast your spell (1-4): ")

        if choice == '1':
            add_quest()
        elif choice == '2':
            show_all_quests()
        elif choice == '3':
            complete_quest()
        elif choice == '4':
            # Save before quitting!
            save_quests()
            print("\nQuest Log saved. Goodbye, adventurer!")
            break  # Exit the while loop
        else:
            print("\nInvalid spell! Try again.")


# --- 5. RUN THE PROGRAM ---
# This standard Python line ensures main() only runs
# when the script is executed directly.
if __name__ == "__main__":
    main()
