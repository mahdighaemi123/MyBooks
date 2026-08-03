import random
 
def roll_dice():
    number = random.randint(1, 6)
    print(f"You rolled a: {number}")
 
# Call the function
roll_dice()