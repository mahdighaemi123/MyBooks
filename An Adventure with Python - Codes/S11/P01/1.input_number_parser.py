print("Enter a number:")
user_input = input()
number = int(user_input) # This line will CRASH if user types "hello"
print("Your number is: " + str(number))