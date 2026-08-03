translator = {"hello": "dorood"}
word_to_find = "cat"

# Check if the 'key' is in the dictionary
if word_to_find in translator:
    print("Translation is:")
    print(translator[word_to_find])
else:
    print("Sorry, that word was not found.") # This will run!