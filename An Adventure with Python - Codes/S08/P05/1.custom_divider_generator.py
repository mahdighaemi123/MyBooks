# 1. We set a default value inside the parenthesis: char="="
def print_divider(char="="):
    # This prints the character 20 times
    print(char * 20)

# Scenario A: The Lazy Way (Using Default)
print("--- Standard Divider ---")
print_divider()  # We gave NO argument, so Python uses "=" automatically.

# Scenario B: The Custom Way (Overriding Default)
print("--- Magic Divider ---")
print_divider("*") # We gave an argument, so "=" is ignored and "*" is used.

print("--- Rich Divider ---")
print_divider("$")