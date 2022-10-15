# c_game_engine.py
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from b_player import Player

class Game:
    def __init__(self):
        self.PLAYER1 = Player()
        self.PLAYER2 = Player()

    def setup(self):
        print("Welcome to Ship, Captain and Crew!")

    def run(self):
        while self.PLAYER1.SCORE < 20 and self.PLAYER2.SCORE < 20:
            # --- PLAYER 1 TURN --- #
            print("Player 1 Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                ROLLS += 1

if __name__ == "__main__":
    GAME = Game()
    GAME.setup()
    GAME.run()
