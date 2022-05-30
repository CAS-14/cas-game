from datetime import datetime
from enum import auto
from operator import inv
from pick import pick
import pickle
import random
import math
import os

savedir = "saves"

class Item:
    def __init__(self, name, description, amount = 1, stack_limit = -1):
        self.name = name
        self.description = description
        self.limit = stack_limit
        self.amount = amount

class Tool(Item):
    def __init__(self, durability, attack, damaged = 0, atk_range = 0.1):
        self.durability = durability
        self.damaged = damaged
        self.broken = False
        self.attack = attack
        self.attack_range = atk_range
        self.limit = 1
        self.amount = 1

    def take_damage(self, damage):
        self.damaged =- damage
        output = f"{self.name} took {damage} damage!"

        if self.damaged >= self.durability:
            self.broken = True
            output += f" {self.name} is broken!"

        return output

    def calc_damage(self):
        return self.attack + (random.randint(0, math.floor(self.attack_range * self.attack)))

class Entity:
    def __init__(self, name, health, attack, inventory: list = [], select: int = 10, atk_mult = 1, def_mult = 1, hel_mult = 1):
        self.name = name
        self.health = health
        self.attack = attack

        self.alive = True

        self.inventory = inventory
        self.select = select
        self.multiplier = {"attack": atk_mult, "defense": def_mult, "health": hel_mult}

    def gain(self, item: Item):
        for owned_item in self.inventory:
            new_amount = owned_item.amount + item.amount
            if type(owned_item) is type(item) and new_amount <= owned_item.limit:
                owned_item.amount = new_amount
                return f"Added {item.name} to your inventory!"

        if len(self.inventory) < 10:
            self.inventory.append(item)
            return f"Added {item.name} to your inventory!"

        return f"Could not add {item.name} to your inventory."

    def attack(self, enemy: "Entity", autoselect: bool = False):
        if autoselect:
            best_weapon = 11
            for tool in self.inventory:
                if tool.attack > best_weapon.attack:
                    best_weapon = tool

            self.select = 

        attack_tool = self.inventory[self.select] if self.select < 10 else self
        base_damage = 
        calc_damage = base_damage + random.randint(-0.1 * base_damage, 0.1 * base_damage)
        enemy.health =- calc_damage

        print(f"You attacked {enemy} with {attack_tool.name}, and dealt {calc_damage} damage!")



class Player:
    def __init__(self, name):
        self.name = name
        self.multiplier = {"attack": 1, "defense": 1, "health": 1}

    def say(self, message):
        print(f"{self.name}: {message}")

    def attack(self, tool: Tool, enemy: Entity):
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
        with open(f"{savedir}/{self.name}.casgame", "wb") as f:
            f.write(pickle.dumps(self))
        
        return "Game saved!"

    def info(self):
        return f"{self.name}: last played {self.last_played}"


def start():
    input("press enter")
    action = pick(["New Game", "Load Game", "Help", "Credits"], "Please choose an action:")[1]

    if action == 0:
        game_name = input("Enter a name for this game: ")
        game_data = input("Enter some data for this game: ")

        game = Game(game_name, game_data)

        print("CREATING NEW GAME")

    elif action == 1:
        games = []
        for save in os.listdir(os.fsencode(savedir)):
            name = os.fsdecode(save)
            if name.endswith(".casgame"):
                with open(f"{savedir}/{name}", "rb") as f:
                    games.append(pickle.loads(f.read()))

        if games == []:
            print("No games found.")
            start()
            return

        game_choices = []
        for game in games:
            game_choices.append(game.info())
        selected_game = games[pick(game_choices, "Select a game:")[1]]

        action = pick(["Load", "Delete", "Repair"], f"Select an action for save {selected_game.name}:")[1]

        if action == 0:
            game = selected_game

        elif action == 1:
            yn = input("Are you sure you want to delete this game? [Y/N] ").lower()

            if yn in ["y", "yes"]:
                os.remove(f"{savedir}/{selected_game.name}.casgame")
                print("Game removed.")
                start()
                return

            else:
                print("Game was not removed.")
                start()
                return

        elif action == 2:
            print("Repair action not available at this time.")
            start()
            return

        else:
            print("ERROR")
            start()
            return

    elif action == 2:
        print("No help yet! Sorry...")
        start()
        return

    elif action == 3:
        print("Created with <3 by CAS. More credits coming soon!")
        start()
        return

    else:
        print("ERROR")
        start()
        return

    print("STARTING/RESUMING GAME")
    print(game.get())

    print("The ending.")

def main():
    print("Welcome to the adventure game!")
    start()

if __name__ == "__main__":
    main()