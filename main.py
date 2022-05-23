from pick import pick
import os
import pickle

import core

savedir = "saves"

def start():
    input("press enter")
    action = pick(["New Game", "Load Game", "Help", "Credits"], "Please choose an action:")[1]

    if action == 0:
        game_name = input("Enter a name for this game: ")
        game_data = input("Enter some data for this game: ")

        game = core.Game(game_name, game_data)

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