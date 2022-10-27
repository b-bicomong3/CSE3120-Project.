# d_main.py inside ship_captain_crew directory
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from c_engine import Game


class Main:
    def __init__(self):
        GAME = Game()
        GAME.setup()
        GAME.menu()
        GAME.run()


if __name__ == "__main__":
    MAIN = Main()
