# --- The Old, Repetitive Way ---
print("--- Adventurer 1 ---")
print("Name: Aria")
print("====================")
print("--- Adventurer 2 ---")
print("Name: Kael")
print("====================")

# --- The New, Clean Way (with a Function) ---

# 1. Define the spell once
def print_divider():
    print("====================")

# 2. Call it whenever we need it
print("--- Adventurer 1 ---")
print("Name: Aria")
print_divider()

print("--- Adventurer 2 ---")
print("Name: Kael")
print_divider()