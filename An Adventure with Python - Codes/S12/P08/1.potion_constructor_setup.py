class Potion:
    # The Constructor Spell (Creating + Setting up)
    # We ask for color and price right at the beginning
    def __init__(self, color, price):
        # Instead of setting them manually later, we do it right here!
        self.color = color  # Put the 'color' input into 'self.color'
        self.price = price  # Put the 'price' input into 'self.price'
        print(f"A new {self.color} potion was created!")

    def show_info(self):
        print(f"Details -> Color: {self.color} | Price: {self.price}")

# --- OLD WAY (The Hard Way) ---
# p1 = Potion()
# p1.color = "Red"
# p1.price = 50


# --- NEW WAY (The Professional Way) ---
# We give the data right when we create the object! One line!
p1 = Potion("Red", 50)
# Output: A new Red potion was created!

p2 = Potion("Blue", 100)
# Output: A new Blue potion was created!

# Checking if it worked
p1.show_info()
