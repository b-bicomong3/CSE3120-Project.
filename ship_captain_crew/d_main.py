# d_main.py inside ship_captain_crew directory
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from c_engine import Game


class Main:
    def __init__(self):
        self.__GAME = Game()
        self.__GAME.setup()

    def menu(self):
        print("""
        1. Rules
        2. One Player (PLY vs PC)
        3. Two Players (PLY1 vs PLY2)
        4. Exit
        """)
        CHOICE = int(input("> "))
        if CHOICE == 1:
            pass
        elif CHOICE == 2:
            self.__GAME.singleRun()
        elif CHOICE == 3:
            self.__GAME.doubleRun()
        elif CHOICE == 4:
            exit()


if __name__ == "__main__":
    MAIN = Main()
    MAIN.menu()