class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at midpoint
        self.energy = 5   # Starting at midpoint
        self.happiness = 5  # Starting at midpoint
        self.tricks = []  # For storing learned tricks
        
    def eat(self):
        """Reduces hunger by 3 (min 0) and increases happiness by 1"""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")
        
    def sleep(self):
        """Increases energy by 5 (max 10)"""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy restored!")
        
    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        if self.energy >= 2:  # Only play if there's enough energy
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play right now.")
            
    def get_status(self):
        """Prints the current state of the pet"""
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'▣' * (10 - self.hunger)}{'□' * self.hunger} ({self.hunger}/10)")
        print(f"Energy: {'▣' * self.energy}{'□' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'♥' * self.happiness}{'♡' * (10 - self.happiness)} ({self.happiness}/10)")
        
    def train(self, trick):
        """Teaches the pet a new trick (bonus)"""
        if self.energy >= 3:  # Training requires energy
            self.energy -= 1
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to learn right now.")
            
    def show_tricks(self):
        """Displays all learned tricks (bonus)"""
        if self.tricks:
            print(f"\n{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")