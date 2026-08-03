class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
        print(f"New Balance: {self.balance}")
 
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn. Remaining: {self.balance}")
        else:
            print("Error: Not enough gold!")
 
# --- Object Creation ---
my_acc = BankAccount("Gimli", 100)
my_acc.deposit(50) # balance = 150
my_acc.withdraw(200) # error!
