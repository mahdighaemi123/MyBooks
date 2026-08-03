import random
  
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
name = input("Enter student name: ")
  
assigned_house = random.choice(houses)
print(f"{name} belongs to... {assigned_house}!")