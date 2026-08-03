# Our translator starts empty
translator = {}

# Add a new word (key-value pair)
translator["hello"] = "salam"
translator["goodbye"] = "khodahafez"

print("Translator after adding words:")
print(translator) # Output: {'hello': 'salam', 'goodbye': 'khodahafez'}

# Change an existing word (update the value)
translator["hello"] = "dorood"
print("Translator after update:")
print(translator) # Output: {'hello': 'dorood', 'goodbye': 'khodahafez'}