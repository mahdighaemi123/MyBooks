def make_juice(fruit_name):
    return fruit_name + " Juice"

# --- Example: Execution Flow ---

# 1. The program starts here
print("--- 1. Start Program ---") 

# The program stops at this line and enters the function.
apple_juice = make_juice("Apple")  # The function is called here.

# 2. The function executes, reaches 'return', stops immediately, and returns the value "Apple Juice".
# 3. Execution returns exactly to this spot, and the returned value is stored in the 'apple_juice' variable.

print("--- 2. Return to Main Line ---")

# Now we can use the final result.
print("My drink is:", apple_juice) 

# Output: My drink is: Apple Juice