class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
 
    def save_to_file(self):
        with open("savefile.txt", "w") as f:
            f.write(f"{self.name},{self.hp}")
        print("Game Saved.")
 
# --- Object Creation ---
player = Hero("Aragorn", 100)
player.save_to_file()
