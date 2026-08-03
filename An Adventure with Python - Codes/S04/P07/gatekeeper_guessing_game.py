# --- The Great Number Guessing Game ---

# 1. Initial Setup
secret_number = 14       # The secret number creates the lock
correct_guess = False    # The gate is currently closed (False)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 20.")

# 2. Start the Loop
# Repeat logic WHILE the guess is NOT correct yet
while correct_guess == False:

    # Get input and VITAL STEP: convert text to integer
    guess_text = input("What is your guess? ")
    guess = int(guess_text)

    # 3. Check Game Logic (The Brain)

    # Scene 1: The guess is correct
    if guess == secret_number:
        print("Excellent! You guessed correctly. The gate opens!")
        correct_guess = True  # We flip the switch to 'True' to END the loop

    # Scene 2: The guess is too low
    elif guess < secret_number:
        print("Your number is too small! Try higher.")

    # Scene 3: The guess is too high (Logic: if not equal and not smaller, it must be bigger)
    else:
        print("Your number is too big! Try lower.")

# 4. End of Game
# This line is outside the while loop (no indentation)
print("Game Over. Thanks for trying!")
