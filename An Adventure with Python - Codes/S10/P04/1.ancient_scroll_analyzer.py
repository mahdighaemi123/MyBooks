# --- The Ancient Scroll Analyzer ---

# 1. The Input Scroll
# We use triple quotes """ for multi-line strings
scroll_text = """
The dragon sleeps in the mountain's heart.
We must retrieve the magic sword.
Only the brave will succeed.
"""

print("--- Analyzing Ancient Scroll ---")
# Let's print the raw text first to see it
print(scroll_text)
print("================================")


# 2. Challenge: Count Characters
# len() on a string counts EVERY character (letters, spaces, newlines)
char_count = len(scroll_text)


# 3. Challenge: Split into words (The Trick)
# .split() cuts the string at every space and puts words into a LIST
word_list = scroll_text.split()

# OPTIONAL: Uncomment the line below to see what the list looks like!
# print(word_list) 


# 4. Challenge: Count Words
# Now len() counts the number of items inside the list (the words)
word_count = len(word_list)


# 5. Challenge: Display results with f-strings
# We use f-strings to insert variables directly into the message
print("--- Text Analysis Results ---")
print(f"Total Characters: {char_count}")
print(f"Total Words:     {word_count}")
print("================================")