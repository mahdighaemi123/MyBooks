# Cafe Menu: Soup, Bread

order = input("What do you want to eat? ")

# We convert input to lowercase immediately to be safe
# Now "Soup", "SOUP", and "soup" all work!
if order.lower() == "soup":
    print("Here is your hot soup!")
else:
    print("We don't have that.")