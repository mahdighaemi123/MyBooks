# 'name' is a PARAMETER (a magic box inside the function)
def greet_by_name(name):
    # 'name' acts like a variable that exists ONLY inside this function
    print("Greetings, " + name + "!")
    print("Welcome to the guild.")

# Now, when we call it, we provide an ARGUMENT (the loot)
# An argument is the *actual data* we pass in.
greet_by_name("Aria") # "Aria" is put into the 'name' box
greet_by_name("Kael") # "Kael" is put into the 'name' box