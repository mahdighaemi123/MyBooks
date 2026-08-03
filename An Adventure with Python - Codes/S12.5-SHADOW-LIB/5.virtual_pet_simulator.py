class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
 
    def eat(self):
        self.hunger -= 10
        print(f"{self.name} is eating...")
 
    def play(self):
        self.energy -= 10
        print(f"{self.name} is playing...")
 
# --- Object Creation ---
dog = Pet("Rex") # create object
dog.eat()        # call eat
dog.play()
