secret_number = 7
user_guess = int(input("Guess a number: "))

if user_guess == secret_number:
    print("Great! You guessed correctly.")

elif user_guess < secret_number:
    print("Your number is too small!")

else:
    # If it is not equal and not smaller, it must be larger.
    print("Your number is too big!")
