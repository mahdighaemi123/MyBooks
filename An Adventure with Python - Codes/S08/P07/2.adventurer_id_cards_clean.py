# --- The Cleaned-Up Spellbook (Using Functions) ---

# 1. --- Define the Reusable Spell (The Machine) ---
# We create ONE function that takes 3 arguments (inputs)
def show_adventurer_stats(name, job_class, hp):
    print("--- Adventurer ID Card ---")
    print("Name: " + name)
    print("Class: " + job_class)
    
    # CRITICAL: We must convert integer 'hp' to string 'str()' to join it!
    print("HP: " + str(hp))
    
    print("==========================")


# 2. --- Call the Spell (Using the Machine) ---
# Our main code is now simple, clean, and easy to read!

# Creating Aria's card
show_adventurer_stats("Aria", "Ranger", 100)

# Creating Kael's card
show_adventurer_stats("Kael", "Mage", 80)

# Want to add a new one? It's just ONE line now!
show_adventurer_stats("Gimli", "Warrior", 150)