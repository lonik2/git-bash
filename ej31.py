import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_dice (self):
        resultado = random.randint (1,self.sides)
        print (f"resultado: {resultado}")

dado = Dice(20)
for i in range(10):
    dado.roll_dice()