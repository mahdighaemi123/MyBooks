# --- The English to Farsi Translator ---

# 1. Setup the Dictionary (Database)
# Structure -> Key (English) : Value (Farsi)
english_to_farsi = {
    "Hello": "سلام",
    "Goodbye": "خداحافظ",
    "Cat": "گربه",
    "Dog": "سگ",
    "House": "خانه",
    "Coder": "برنامه‌نویس"
}

print("Welcome to the Smart Translator!")
print("--- Type 'quit' to exit ---")

# 2. Start the main loop (Infinite Loop)
# We use 'while True' to keep running forever until 'break'
while True:
    print("--------------------")
    
    # Get input from the user
    word = input("Enter an English word to translate: ")
 
    # 3. Check for exit command FIRST
    if word == "quit":
        print("Goodbye, Adventurer!")
        break  # The spell to smash the loop and exit!

    # 4. Search logic (Safety Spell)
    # check IF the word exists inside the dictionary keys
    if word in english_to_farsi:
        # Get the translation
        translation = english_to_farsi[word]
        print("Meaning: " + translation)
    else:
        # If the word is NOT in the dictionary
        print("Sorry, I don't know that word yet.")