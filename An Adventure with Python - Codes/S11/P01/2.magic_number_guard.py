print("Enter a magic number:")
user_input = input()

try:
   # We "try" to run the dangerous code
    number = int(user_input)
    print(f"Your magic number is: {number}")
except:
   # If the 'try' block fails, this code runs instead
    print("That wasn't a number, adventurer! Spell failed.")