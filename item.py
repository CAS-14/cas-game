import random
import math

class Item:
    def __init__(self, name, description, durability = -1):
        self.name = name
        self.description = description

class Tool(Item):
    def __init__(self, durability, attack, damaged = 0, atk_range = 0.1):
        self.durability = durability
        self.damaged = damaged
        self.broken = False
        self.attack = attack
        self.attack_range = atk_range

    def take_damage(self, damage):
        self.damaged =- damage
        output = f"{self.name} took {damage} damage!"

        if self.damaged >= self.durability:
            self.broken = True
            output += f" {self.name} is broken!"

        return output

    def calc_damage(self):
        return self.attack + (random.randint(0, math.floor(self.attack_range * self.attack)))

