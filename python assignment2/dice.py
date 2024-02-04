import random
class Dice:
    def __init__(self):
        self.number = random.randint(1, 6)
    def roll(self):
        self.number = random.randint(1, 6)
    def get_number(self):
        return self.number
dice1 = Dice()
print(dice1.get_number())
dice1.roll()
print(dice1.get_number())

