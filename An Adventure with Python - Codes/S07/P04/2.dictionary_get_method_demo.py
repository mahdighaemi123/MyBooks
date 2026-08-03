translator = {"hello": "dorood"}

# Get the translation for 'hello'
translation_1 = translator.get("hello")
print(translation_1) # Output: dorood

# Get the translation for 'cat'
translation_2 = translator.get("cat", "Word not found.")
print(translation_2) # Output: Word not found. (No crash!)