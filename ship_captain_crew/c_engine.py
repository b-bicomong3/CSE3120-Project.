# c_engine.py inside ship_captain_crew directory
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from b_player import Player


class Game:
    def __init__(self):
        self.PLAYER1 = None
        self.PLAYER2 = None
        self.__DEALER = Player("Dealer")

    def setup(self):
        print("Welcome to Ship, Captain and Crew!")
        print("""
              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
        """)

    def rules(self):
        """

        :return:
        """
        print("""
        """)

    def singleRun(self):
        PLAYER_NAME = input("Player Name: ")
        self.PLAYER1 = Player(PLAYER_NAME)
        while self.PLAYER1.SCORE <= 20 and self.__DEALER.SCORE <= 20:
            # --- PLAYER 1 TURN --- #
            print(f"{self.PLAYER1.getName()}'s Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                ROLLS += 1
                if ROLLS != 3 and len(self.PLAYER1.DICE) > 2:
                    self.PLAYER1.reroll()
                    input("Re-roll! (To continue press enter)")

            if ROLLS == 3 and len(self.PLAYER1.DICE) > 2:
                print("You weren't able to get all the requirements")
            elif ROLLS < 3 and len(self.PLAYER1.DICE) == 2:
                TEMP_SCORE = self.PLAYER1.Score()
                print(f"Would you like to keep {TEMP_SCORE} pieces of gold? (y/N)")
                CHOICE = input("> ")
                if CHOICE.upper() == "N":
                    self.PLAYER1.rollDice()
                    print("Remaining Dice:")
                    for die in self.PLAYER1.DICE:
                        die.displayDie()
            if ROLLS == 3 and len(self.PLAYER1.DICE) == 2:
                self.PLAYER1.SCORE = self.PLAYER1.Score()
                print(f"Your total amount of booty is {self.PLAYER1.SCORE}")

            self.PLAYER1.reset()
            # --- DEALER TURN --- #
            print("Dealer Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.__DEALER.DICE) > 2:
                self.__DEALER.rollDice()
                self.__DEALER.holdDie()
                ROLLS += 1
                if ROLLS != 3 and len(self.__DEALER.DICE) > 2:
                    self.__DEALER.reroll()
                    print("Re-roll!")

            if ROLLS == 3 and len(self.__DEALER.DICE) > 2:
                print("Dealer wasn't able to get all the requirements")
            elif ROLLS < 3 and len(self.__DEALER.DICE) == 2:
                SCORE = self.__DEALER.Score()
                if SCORE < 6:
                    self.__DEALER.rollDice()
                    print("Remaining Dice:")
                    for die in self.__DEALER.DICE:
                        die.displayDie()
            if ROLLS == 3 and len(self.__DEALER.DICE) == 2:
                SCORE = self.__DEALER.Score()
                print(f"Dealer's total amount of booty is {SCORE}")

            self.__DEALER.reset()

        if self.PLAYER1.SCORE > self.__DEALER.SCORE:
            print("Player 1 Wins!")
        else:
            print("Dealer Wins")
        exit()

    def doubleRun(self):
        PLAYER_NAME1 = input("Player Name: ")
        self.PLAYER1 = Player(PLAYER_NAME1)
        PLAYER_NAME2 = input("Player Name: ")
        self.PLAYER2 = Player(PLAYER_NAME2)
        while self.PLAYER1.SCORE <= 20 and self.PLAYER2.SCORE <= 20:
            # --- PLAYER 1 TURN --- #
            print(f"{self.PLAYER1.getName()}'s Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                self.PLAYER1.rollDice()
                self.PLAYER1.holdDie()
                ROLLS += 1
                if ROLLS != 3 and len(self.PLAYER1.DICE) > 2:
                    self.PLAYER1.reroll()
                    input("Re-roll! (To continue press enter)")

            if ROLLS == 3 and len(self.PLAYER1.DICE) > 2:
                print("You weren't able to get all the requirements")
            if ROLLS > 3 and len(self.PLAYER1.DICE) == 2:
                TEMP_SCORE = self.PLAYER1.Score()
                print(f"Would you like to keep {TEMP_SCORE} pieces of gold? (y/N)")
                CHOICE = input("> ")
                if CHOICE.upper() == "Y":
                    SCORE = self.PLAYER1.addScore(TEMP_SCORE)
                    print(f"Your total amount of booty is {SCORE}")
                else:
                    self.PLAYER1.reroll()
            if self.PLAYER1.SCORE >= 20:
                break
            self.PLAYER1.resetDie()

            # --- PLAYER 2 TURN --- #
            print(f"{self.PLAYER2.getName()}'s Turn!")
            ROLLS = 0
            while ROLLS < 3 and len(self.PLAYER2.DICE) > 2:
                self.PLAYER2.rollDice()
                self.PLAYER2.holdDie()
                ROLLS += 1
                if ROLLS != 3 and len(self.PLAYER2.DICE) > 2:
                    self.PLAYER2.reroll()
                    input("Re-roll! (To continue press enter)")

            if ROLLS == 3 and len(self.PLAYER2.DICE) > 2:
                print("You weren't able to get all the requirements")
            else:
                TEMP_SCORE = self.PLAYER2.Score()
                print(f"Would you like to keep {TEMP_SCORE} pieces of gold? (y/N)")
                CHOICE = input("> ")
                if CHOICE.upper() == "Y":
                    SCORE = self.PLAYER2.addScore(TEMP_SCORE)
                    print(f"Your total amount of booty is {SCORE}")
                    if self.PLAYER2.SCORE >= 20:
                        break
            self.PLAYER2.resetDie()
        if self.PLAYER1.SCORE > self.PLAYER2.SCORE:
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins")
        exit()


if __name__ == "__main__":
    GAME = Game()
    #    GAME.setup()
    #    GAME.menu()
    GAME.run()
