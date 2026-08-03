# --- The Adventurer's Backpack Manager ---
 
# 1. Setup the Memory (The Backpack)
# WARNING: We create the list OUTSIDE the loop.
# If we put it inside, it would be wiped clean every time the loop runs!
backpack = []
is_running = True
 
print("Welcome to your Adventure Backpack!")
print("Commands: 'add', 'remove', 'show', 'quit'")
 
# 2. Start the Engine (The Loop)
# The program stays alive as long as is_running is True
while is_running == True:
    print("--------------------")
    
    # 3. Get command from user (Listening)
    command = input("What is your command? ")
 
    # 4. Make decisions based on command (The Brain)
    
    # --- ADD COMMAND (Pick up item) ---
    if command == "add":
        item = input("What item did you find? ")
        backpack.append(item) 
        print(item + " added to backpack.")
 
    # --- REMOVE COMMAND (Drop item) ---
    elif command == "remove":
        item = input("What item to drop? ")
        
        # Safety Check: Is the item actually in the backpack?
        if item in backpack:
            backpack.remove(item)
            print(item + " dropped.")
        else:
            # If item is NOT in the list, tell the user instead of crashing
            print("Error: You don't have " + item + " in your backpack!")
 
    # --- SHOW COMMAND (Check Inventory) ---
    elif command == "show":
        print("--- Your Inventory ---")
        
        # Check if backpack is empty first
        if len(backpack) == 0:
            print("Your backpack is empty.")
        else:
            # Loop through the list to show items nicely
            for item in backpack:
                print("- " + item)
 
    # --- QUIT COMMAND (Rest) ---
    elif command == "quit":
        print("Safe travels, Adventurer!")
        # This turns off the 'while' loop and stops the program
        is_running = False 
 
    # --- INVALID COMMAND ---
    else:
        # If the user types something like "dance" or "fly"
        print("I don't know that spell (command).")
 
# 5. End of program
print("System Closed.")