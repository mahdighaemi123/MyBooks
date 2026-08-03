# Create a variable to control the game state
game_over = False

while game_over == False:
    # The lines below repeat constantly because they are indented
    print("The game is running...")
    
    answer = input("Do you want to end the game? (yes/no) ")
    
    if answer == "yes":
        game_over = True  # This makes the loop condition False, stopping the loop

print("Goodbye!")