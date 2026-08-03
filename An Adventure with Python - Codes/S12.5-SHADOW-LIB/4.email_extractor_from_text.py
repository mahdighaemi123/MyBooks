with open("data.txt", "r") as file:
    words = file.read().split()
 
with open("emails.txt", "w") as output:
    for word in words:
        if "@" in word and "." in word:
            output.write(word + "\n")
            
print("Emails extracted.")
