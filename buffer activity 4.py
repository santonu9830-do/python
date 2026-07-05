class dad:

    def __init__(self, eyes, aggressiveness):
        self.eyes = eyes
        self.aggressiveness = aggressiveness
    def display(self):
        print("Eyes:", self.eyes)
        print("Aggressiveness:", self.aggressiveness)


class son(dad):
    def __init__(self, age, name, eyes, aggressiveness):
        self.age = age
        self.name = name
        super().__init__(eyes, aggressiveness)

obj = son(20, "Santonu", "Black", "High")

obj.display()
        