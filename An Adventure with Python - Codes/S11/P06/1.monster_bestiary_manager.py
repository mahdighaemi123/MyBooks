import json  # Import the magic library to handle data

# --- The File Name ---
book_file = "bestiary.json"

# --- Step 1: The Load Spell ---
# We try to open the existing book. If it doesn't exist, we start a new one.
try:
    with open(book_file, "r") as f:
        bestiary = json.load(f)  # Load the dictionary from the file
    print("Bestiary loaded! Ancient knowledge is ready.")
except:
    # This block runs if the file is missing (first time running)
    print("No book found. Starting a new blank Bestiary.")
    bestiary = {}  # Create an empty dictionary

# --- The Main Program Loop ---
while True:
    print("\n" + "*"*30)
    print("Monster Hunter Menu:")
    print("1. Add a new Monster")
    print("2. Find Weakness (Search)")
    print("3. Save & Exit")
    
    choice = input("Choose an option (1-3): ")

    # --- Option 1: Learn a new monster ---
    if choice == "1":
        monster = input("Enter Monster Name: ")
        weakness = input(f"What is the weakness of {monster}? ")
        
        # Save to dictionary (Key = Monster, Value = Weakness)
        bestiary[monster] = weakness
        print(f"Recorded: {monster} is weak against {weakness}.")

    # --- Option 2: Search for battle ---
    elif choice == "2":
        monster = input("What monster are you fighting? ")
        
        # Check if the monster exists in our dictionary keys
        if monster in bestiary:
            # Get the value (weakness) using the key (monster name)
            print(f"ADVICE: Use [{bestiary[monster]}] to defeat it!")
        else:
            print("DANGER! Unknown monster. Run away!")

    # --- Option 3: The Save Spell ---
    elif choice == "3":
        print("Saving knowledge to file...")
        
        # Open the file in 'write' mode ('w')
        with open(book_file, "w") as f:
            json.dump(bestiary, f)
            
        print("Book closed. Goodbye Hunter!")
        break  # Break the loop to stop the program

    else:
        print("Invalid option. Try again.")