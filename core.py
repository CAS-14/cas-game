import pickle
from datetime import datetime
import random

import main
import item
import npc

class Player:
    def __init__(self, name):
        self.name = name
        self.multiplier = {"attack": 1, "defense": 1, "health": 1}

    def say(self, message):
        print(f"{self.name}: {message}")

    def attack(self, tool: item.Tool, enemy: npc.Creature):
        print(f"You attacked {enemy} with {tool}!")
        damage = enemy.take_damage(tool.calc_damage() * self.multiplier["attack"])
        print(f"Attack dealt {damage} damage!")
        tool_damage = tool.take_damage(random.randint(2, 10))


class Game:
    def __init__(self, save_name, data):
        self.name = save_name.replace(".", "_")
        self.data = data
        self.last_played = str(datetime.now()).split(".")[0]

        self.save()

    def get(self):
        return self.data

    def save(self):
        with open(f"{main.savedir}/{self.name}.casgame", "wb") as f:
            f.write(pickle.dumps(self))
        
        return "Game saved!"

    def info(self):
        return f"{self.name}: last played {self.last_played}"

def test():
    print("hi")