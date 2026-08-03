# A raw data string (items separated by commas)
raw_data = "Sword,Shield,Potion,Map"
 
# We tell Python: "Cut the string wherever you see a COMMA"
inventory = raw_data.split(",")

print(inventory)
# Output: ['Sword', 'Shield', 'Potion', 'Map']