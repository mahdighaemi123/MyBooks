class Bomb:
    def __init__(self, start_time):
        self.time = start_time
 
    def tick(self):
        if self.time > 0:
            self.time -= 1
            print(f"Tick... {self.time}")
        if self.time == 0:
            print("BOOM!")
 
# --- Object Creation ---
tnt = Bomb(3)
tnt.tick() # 2
tnt.tick() # 1
tnt.tick() # BOOM!
