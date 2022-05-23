import pickle
from datetime import datetime

import main

class Player:
    def __init__(self, name):
        self.name = name

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