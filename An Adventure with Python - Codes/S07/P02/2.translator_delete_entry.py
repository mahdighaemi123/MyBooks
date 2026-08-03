translator = {"hello": "salam", "goodbye": "khodahafez"}
print("Translator before delete:")
print(translator)

# Delete the word 'hello'
del translator["hello"]

print("Translator after delete:")
print(translator) # Output: {'goodbye': 'khodahafez'}