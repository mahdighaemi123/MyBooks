password = "123"
guess = input("Enter password: ")

if guess == password:
    # We have an indentation (Tab) here.
    # This block runs ONLY if the condition is True
    print("Access Granted: Open the door")

else:
    # We have an indentation (Tab) here too.
    # This block runs if the condition is False (Wrong password).
    print("Access Denied: Enable alarm")

# This line has NO indentation.
# It is outside the if/else blocks and always runs.
print("Continue program...")