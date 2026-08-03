print("--- Enter prices (Type 0 to finish) ---")
total = 0

while True:
    price = float(input("Price: $"))
    
    # If price is 0, stop the loop
    if price == 0:
        break
        
    # Add price to total
    total = total + price

print(f"Total Bill: ${total}")