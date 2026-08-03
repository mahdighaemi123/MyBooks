class Potion:
    # We MUST pass 'self' as the first argument to access the object's own data
    def show_color(self):
        # self.color translates to: "Go inside ME and find the 'color' variable"
        print(f"My color is {self.color}")
 
# Setup objects
p1 = Potion()
p1.color = "Red"
 
p2 = Potion()
p2.color = "Blue"
 
# Magic of self
p1.show_color()
# Python secretly does this: show_color(p1) -> self becomes p1 -> prints "Red"
 
p2.show_color()
# Python secretly does this: show_color(p2) -> self becomes p2 -> prints "Blue"