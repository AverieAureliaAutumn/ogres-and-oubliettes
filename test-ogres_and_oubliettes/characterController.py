import random
import Ai

class action:
    def __init__(self):
        pass
    def attack(self,enemy):
        hit = random.randrange(10)
        enemy.health -= hit


        print(": You attack for: "+ hit)
        





