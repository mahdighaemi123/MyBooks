numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
  
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
  
print(f"Clean list: {unique_numbers}")