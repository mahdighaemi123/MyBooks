import json                   # For eternal memory (Chapter 11)
import datetime               # For time magic (Chapter 14)
from quest_model import Quest  # Our own blueprint! (Chapter 13)

# Global variables (our magic scrolls)
quest_list = []  # This is our main "backpack" for quests
SAVE_FILE = "quest_log.json"  # The name of our eternal memory file"


def add_quest():
    print("\n--- Add New Quest ---")

    # Input Validation Loop for Title
    while True:
        title = input("Enter quest title: ").strip()
        if title:  # If title is not empty
            break
        print("Error: Title cannot be empty! Try again.")

    description = input("Enter quest description: ").strip()

    # Create and add
    new_quest = Quest(title, description)
    quest_list.append(new_quest)
    print("\n[Quest added successfully!]")


def delete_quest():
    show_all_quests()  # Show list so user knows the numbers

    if not quest_list:
        return

    try:
        choice = int(input("Enter number to DELETE: ")) - 1

        if 0 <= choice < len(quest_list):
            removed = quest_list.pop(choice)  # Removes item from list
            print(f"\n[Quest '{removed.title}' has been deleted forever!]")
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")


def show_all_quests():
    print("\n--- Your Quest Log ---")
    if not quest_list:
        print("Log is empty.")
        return

    # Ask for filter mode
    print("1. Show All")
    print("2. Show Pending Only")
    mode = input("Choose view mode (1/2): ")

    for index, quest in enumerate(quest_list):
        # Filter Logic
        if mode == '2' and quest.status == "Complete":
            continue  # Skip this iteration if quest is complete

        print(f"\n--- Quest {index + 1} ---")
        quest.display_info()
        print("--------------------")


def edit_quest():
    show_all_quests()
    if not quest_list:
        return

    try:
        index = int(input("Enter number to EDIT: ")) - 1
        if 0 <= index < len(quest_list):
            quest = quest_list[index]

            print(f"Editing '{quest.title}'...")

            # Get new data (leave empty to keep old)
            new_title = input(f"New Title [{quest.title}]: ").strip()
            new_desc = input(
                f"New Description [{quest.description}]: ").strip()

            if new_title:
                quest.title = new_title
            if new_desc:
                quest.description = new_desc

            print("[Quest updated!]")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")


# In main.py
total_xp = 0  # Global variable


def save_quests():
    data = {
        "xp": total_xp,
        "quests": []
    }

    # Add quests to data
    for q in quest_list:
        data["quests"].append({
            "title": q.title,
            "description": q.description,
            "status": q.status,
            # Add other fields like deadline/priority here too
        })

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_quests():
    global quest_list, total_xp
    try:
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)

            # Load XP (if it exists, otherwise 0)
            total_xp = data.get("xp", 0)

            # Load Quests
            data_list = data.get("quests", [])
            for item in data_list:
                # Create a new quest object
                quest = Quest(item['title'], item['description'])
                # Restore its saved data
                quest.status = item['status']
                quest.created_at = datetime.datetime.fromisoformat(
                    item['created_at'])
                quest_list.append(quest)

    except FileNotFoundError:
        print("No save file.")


def search_quest():
    keyword = input("Search for: ").lower()
    found = False

    print(f"\n--- Search Results for '{keyword}' ---")
    for q in quest_list:
        if keyword in q.title.lower():
            q.display_info()
            print("---")
            found = True

    if not found:
        print("No quests found.")


def reset_data():
    confirm = input(
        "WARNING: This will delete ALL quests and XP. Are you sure? (yes/no): ")

    if confirm.lower() == "yes":
        global quest_list, total_xp
        quest_list = []
        total_xp = 0

        # Overwrite file with empty data
        with open(SAVE_FILE, "w") as f:
            f.write("{}")

        print("[Memory Wiped. Fresh Start!]")
    else:
        print("[Reset cancelled.]")


def export_to_txt():
    filename = "my_quest_log.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"ADVENTURER QUEST LOG - XP: {total_xp}\n")
        f.write("="*30 + "\n")

        for i, q in enumerate(quest_list, 1):
            f.write(f"{i}. {q.title} [{q.status}]\n")
            f.write(f"   Desc: {q.description}\n")
            f.write("-" * 20 + "\n")

    print(f"[Exported successfully to {filename}]")


def complete_quest():
    """
    Asks the user which quest to mark as complete.
    """
    global total_xp

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
            total_xp += 10
        else:
            print("Invalid quest number! No quest was completed.")

    except ValueError:
        print("That's not a number! Spell failed.")


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
        print("5. Delete a quest")
        print("6. Edit a quest")
        print("7. Search for a quest")
        print("8. Export to .txt")
        print("9. RESET ALL DATA")
        print("====================================")
        choice = input("Cast your spell (1-4): ")

        if choice == '1':
            add_quest()
        elif choice == '2':
            show_all_quests()
        elif choice == '3':
            complete_quest()
        elif choice == '4':
            save_quests()
            print("\nQuest Log saved. Goodbye, adventurer!")
            break
        elif choice == '5':
            delete_quest()
        elif choice == '6':
            edit_quest()
        elif choice == '7':
            search_quest()
        elif choice == '8':
            export_to_txt()
        elif choice == '9':
            reset_data()
        else:
            print("\nInvalid spell! Try again.")


if __name__ == "__main__":
    main()
