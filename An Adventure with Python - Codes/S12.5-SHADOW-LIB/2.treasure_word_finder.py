search_word = input("Enter word to search: ")
 
with open("my_file.txt", "r") as file:
    content = file.read()
    
    if search_word in content:
        print("Found!")
    else:
        print("Not Found.")
