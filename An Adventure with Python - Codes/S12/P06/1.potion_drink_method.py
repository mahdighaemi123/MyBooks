class Potion:
    # A method is just a function defined INSIDE the class
    # It defines an action the object can DO.
    def drink(self):
        print("Gulp gulp... You drank the potion!")
 
# Create object
p1 = Potion()
 
# Call the behavior (method) using the dot (.)
p1.drink()
# Output: Gulp gulp... You drank the potion!