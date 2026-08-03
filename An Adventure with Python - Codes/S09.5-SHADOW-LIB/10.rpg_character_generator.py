import random
  
def create_character():
    names = ["Arthur", "Merlin", "Lancelot"]
    roles = ["Warrior", "Mage", "Archer"]
    
    character = {
        "Name": random.choice(names),
        "Role": random.choice(roles),
        "Health": random.randint(50, 100),
        "Power": random.randint(10, 20)
    }
    return character
  
# Create a new hero
hero = create_character()
print(hero)