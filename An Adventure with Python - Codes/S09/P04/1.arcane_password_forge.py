import random  # We need this wizard to generate random things!

# --- 1. The Ingredients (Manual Entry) ---
# We define the 4 types of characters we want in our password
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# --- 2. Mixing the Soup ---
# Combine all ingredients into one big pool of characters
all_characters = lowercase_letters + uppercase_letters + numbers + symbols

# --- 3. Magic Configuration ---
password_length = 12   # How long should the password be?
password = ""          # We start with an empty string

# --- 4. Casting the Spell (The Loop) ---
# We loop 12 times. inside the loop, we pick one char and add it.
for _ in range(password_length):
    # Pick one random character from the big pool
    random_char = random.choice(all_characters)
    
    # Add it to our password variable
    password = password + random_char  # OR: password += random_char

# --- 5. Reveal the Secret ---
print("---------------------------------")
print(f"Your secure password is: {password}")
print("---------------------------------")