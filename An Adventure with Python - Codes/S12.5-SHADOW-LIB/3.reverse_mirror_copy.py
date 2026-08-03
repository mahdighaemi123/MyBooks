# Read from source
with open("source.txt", "r") as reader:
    content = reader.read()
 
reversed_content = content[::-1]
 
# Write to mirror file
with open("mirror.txt", "w") as writer:
    writer.write(reversed_content)
    print("Mirror file created.")
