prices = {"Apple": 10, "Banana": 5, "Orange": 7}
cart = ["Apple", "Apple", "Banana"]
  
total = 0
for item in cart:
    if item in prices:
        total += prices[item]
  
print(f"Total Bill: ${total}")