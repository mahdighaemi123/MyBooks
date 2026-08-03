text = input("Enter a sentence: ")
vowels = "aeiou"
count = 0
  
for char in text:
    if char.lower() in vowels:
        count += 1
  
print(f"Number of vowels: {count}")