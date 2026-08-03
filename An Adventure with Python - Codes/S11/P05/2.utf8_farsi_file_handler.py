# --- The "Safe Way" for all languages ---

# Writing Farsi safely
with open("farsi_scroll.txt", "w", encoding="utf-8") as f:
    f.write("سلام ماجراجو!")

# Reading Farsi safely
with open("farsi_scroll.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content) # Output: سلام ماجراجو!