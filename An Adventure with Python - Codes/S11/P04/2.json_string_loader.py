import json
# Imagine we received this text from the internet
received_data = '["Ali", "Reza", "Sina"]'  # This is a String!

# Convert the text back to a REAL Python List
# loads = Load String
real_list = json.loads(received_data)

print(real_list[0]) # Output: Ali
# Now we can use it like a normal list (indexing, loops, etc.)