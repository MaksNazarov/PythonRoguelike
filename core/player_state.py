class PlayerState:
    def __init__(self):
        self.gold = 0
        self.level = 1

    def add_gold(self):
        self.gold += 1
        print(f"You picked up 1 gold. Total: {self.gold}")

    def advance_level(self):
        self.level += 1
        print(f"You are now on level {self.level}")

    def reset(self):
        self.gold = 0
        self.level = 1