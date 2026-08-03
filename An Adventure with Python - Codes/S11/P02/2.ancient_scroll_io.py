# --- STEP 1: WRITE MODE (Create/Overwrite) ---
# We open 'scroll.txt' with "w". 
# WARNING: If scroll.txt existed, it is now empty!
# 'f' is our magic pen to write in this file.
with open("scroll.txt", "w") as f:
    f.write("Chapter 1: The Beginning\n") # \n moves cursor to next line
    f.write("The hero woke up in a dark forest.\n")

# --- STEP 2: APPEND MODE (Add to end) ---
# We open with "a". The old text stays safe.
# We add new lines to the bottom.
with open("scroll.txt", "a") as f:
    f.write("Chapter 2: The Journey\n")
    f.write("He picked up his rusty sword.") 

# --- STEP 3: READ MODE (Retrieve info) ---
# We open with "r". We can ONLY read.
print("--- Reading from the Ancient Scroll ---")
with open("scroll.txt", "r") as f:
    # f.read() pulls ALL text from the file into a variable
    full_text = f.read()
    print(full_text)