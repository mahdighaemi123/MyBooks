# main.py
# Our main program

# We import the spells.py module (file) that we just created
import spells

print("Main program started...")

# To use the spells, we must reference the book (module) name
# Just like we did with random.choice()
spells.greet_adventurer("Aria")
spells.print_divider()
spells.greet_adventurer("Gandalf")
spells.print_divider("-")
