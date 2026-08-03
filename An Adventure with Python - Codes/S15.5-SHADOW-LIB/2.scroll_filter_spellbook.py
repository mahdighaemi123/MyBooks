scrolls = ["Fireball", "Ice", "Fly", "Arcane", "Freeze"]

# Filter: Starts with 'F' AND length > 3
valid_scrolls = [s for s in scrolls if s.startswith("F") and len(s) > 3]

print(valid_scrolls)
