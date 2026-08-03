translator = {"hello": "dorood", "goodbye": "khodāhāfez"}

print("--- Dictionary Keys ---")
for word in translator:
    print(word)

print("--- Dictionary Values ---")
for meaning in translator.values():
    print(meaning)

print("--- Full Translator ---")
# .items() gives us (key, value) pairs
for word, meaning in translator.items():
    print(word + " means " + meaning)