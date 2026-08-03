print("--- Coffee Price: $3.50 ---")
cash = float(input("Insert money: $"))

if cash < 3.50:
    print("Not enough money. Money returned.")
else:
    change = cash - 3.50
    print("Here is your coffee")
    print(f"Your change is: ${change}")