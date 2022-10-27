# c_engine.py inside ship_captain_crew directory
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from b_player import Player


class Game:
    def __init__(self):
        self.__DEALER = Player("Dealer")
        self.PLAYER1 = None
        self.PLAYER2 = None
        self.CHOICE = None

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
Boat ASCII from https://www.asciiart.eu/vehicles/boats
        """)

    def rules(self):
        """

        :return:
        """
        print("""hello
        """)

    def menu(self):
        print("""
            1. Rules
            2. One Player (PLY vs PC)
            3. Two Players (PLY1 vs PLY2)
            4. Exit
            """)
        self.CHOICE = int(input("> "))
        return self.CHOICE

    def __int__(self):
        return self.CHOICE

    def run(self):
        if self.CHOICE == 1:
            print("1")
        elif self.CHOICE == 2:
            # SINGLE PLAYER
            PLAYER_NAME = input("Player Name: ")
            self.PLAYER1 = Player(PLAYER_NAME)
            while self.PLAYER1.isWinner() is False and self.__DEALER.isWinner() is False:
                # --- PLAYER 1 TURN --- #
                print(f"{self.PLAYER1.getName()}'s Turn")
                ROLLS = 0
                while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                    self.PLAYER1.rollDice()
                    self.PLAYER1.holdDie()
                    ROLLS += 1
                    if ROLLS != 3 and len(self.PLAYER1.DICE) > 2:
                        self.PLAYER1.reroll()

                self.PLAYER1.displayResult()
                self.PLAYER1.displayDice()

                if ROLLS == 3 and len(self.PLAYER1.DICE) > 2:
                    input("You weren't able to get all the requirements (Press ENTER to continue)")

                while ROLLS < 3 and len(self.PLAYER1.DICE) == 2:
                    self.PLAYER1.TEMP_SCORE = self.PLAYER1.Points()
                    print(f"Rolls: {ROLLS}")
                    print(f"Would like to keep {self.PLAYER1.TEMP_SCORE} pieces of gold? (Y/n)")
                    OPTION = input("> ")
                    if OPTION.upper() == "N":
                        self.PLAYER1.TEMP_SCORE = 0
                        self.PLAYER1.POINTS = 0
                        self.PLAYER1.rollDice()
                        self.PLAYER1.displayDice()
                        ROLLS += 1
                    else:
                        print(f"Rolls: {ROLLS}")
                        self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                        input(f"Your total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")
                        break

                if ROLLS == 3 and len(self.PLAYER1.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    if self.PLAYER1.TEMP_SCORE == 0:
                        self.PLAYER1.TEMP_SCORE = self.PLAYER1.Points()
                    self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                    input(f"Your total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")

                self.PLAYER1.reset()

                if self.PLAYER1.SCORE >= 20:
                    continue

                # --- DEALER TURN --- #
                print(f"{self.__DEALER.getName()}'s Turn")
                ROLLS = 0
                while ROLLS < 3 and len(self.__DEALER.DICE) > 2:
                    self.__DEALER.rollDice()
                    self.__DEALER.holdDie()
                    ROLLS += 1
                    if ROLLS != 3 and len(self.__DEALER.DICE) > 2:
                        self.__DEALER.reroll()

                self.__DEALER.displayResult()

                if ROLLS == 3 and len(self.__DEALER.DICE) > 2:
                    input("Dealer wasn't able to get all the requirements (Press ENTER to continue)")

                while ROLLS < 3 and len(self.__DEALER.DICE) == 2:
                    self.__DEALER.TEMP_SCORE = self.__DEALER.Points()
                    if self.__DEALER.TEMP_SCORE >= 5:
                        D_OPTION = 1
                    else:
                        D_OPTION = 2
                    if D_OPTION == 1:
                        self.__DEALER.TEMP_SCORE = 0
                        self.__DEALER.POINTS = 0
                        self.__DEALER.rollDice()
                        ROLLS += 1
                    elif D_OPTION == 2:
                        print(f"Rolls: {ROLLS}")
                        self.__DEALER.displayDice()
                        self.__DEALER.SCORE = self.__DEALER.addScore(self.__DEALER.TEMP_SCORE)
                        input(f"Dealer's amount of booty is {self.__DEALER.SCORE} (Press ENTER to continue)")
                        break

                if ROLLS == 3 and len(self.__DEALER.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    self.__DEALER.displayDice()
                    if self.__DEALER.TEMP_SCORE == 0:
                        self.__DEALER.TEMP_SCORE = self.__DEALER.Points()
                    self.__DEALER.SCORE = self.__DEALER.addScore(self.__DEALER.TEMP_SCORE)
                    input(f"Dealer's total amount of booty is {self.__DEALER.SCORE} (Press ENTER to continue)")

                self.__DEALER.reset()

            if self.PLAYER1.SCORE > self.__DEALER.SCORE:
                print("Player 1 Wins!")
            else:
                print("Dealer Wins")
            return Game()

        elif self.CHOICE == 3:
            # TWO PLAYERS
            PLAYER_NAME1 = input("Player Name: ")
            self.PLAYER1 = Player(PLAYER_NAME1)
            PLAYER_NAME2 = input("Player Name: ")
            self.PLAYER2 = Player(PLAYER_NAME2)
            while self.PLAYER1.isWinner() is False and self.__DEALER.isWinner() is False:
                # --- PLAYER 1 TURN --- #
                print(f"{self.PLAYER1.getName()}'s Turn")
                ROLLS = 0
                while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                    self.PLAYER1.rollDice()
                    self.PLAYER1.holdDie()
                    ROLLS += 1
                    if ROLLS != 3 and len(self.PLAYER1.DICE) > 2:
                        self.PLAYER1.reroll()

                self.PLAYER1.displayResult()
                self.PLAYER1.displayDice()

                if ROLLS == 3 and len(self.PLAYER1.DICE) > 2:
                    input(f"{self.PLAYER1.getName()} wasn't able to get all the requirements (Press ENTER to continue)")

                while ROLLS < 3 and len(self.PLAYER1.DICE) == 2:
                    self.PLAYER1.TEMP_SCORE = self.PLAYER1.Points()
                    print(f"Rolls: {ROLLS}")
                    print(f"Would like to keep {self.PLAYER1.TEMP_SCORE} pieces of gold? (Y/n)")
                    OPTION = input("> ")
                    if OPTION.upper() == "N":
                        self.PLAYER1.TEMP_SCORE = 0
                        self.PLAYER1.POINTS = 0
                        self.PLAYER1.rollDice()
                        self.PLAYER1.displayDice()
                        ROLLS += 1
                    else:
                        print(f"Rolls: {ROLLS}")
                        self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                        input(f"{self.PLAYER1.getName()}'s total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")
                        break

                if ROLLS == 3 and len(self.PLAYER1.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    if self.PLAYER1.TEMP_SCORE == 0:
                        self.PLAYER1.TEMP_SCORE = self.PLAYER1.Points()
                    self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                    input(
                        f"{self.PLAYER1.getName()}'s total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")

                self.PLAYER1.reset()

                # --- PLAYER 2 TURN --- #
                print(f"{self.PLAYER2.getName()}'s Turn")
                ROLLS = 0
                while ROLLS < 3 and len(self.PLAYER2.DICE) > 2:
                    self.PLAYER2.rollDice()
                    self.PLAYER2.holdDie()
                    ROLLS += 1
                    if ROLLS != 3 and len(self.PLAYER2.DICE) > 2:
                        self.PLAYER2.reroll()

                self.PLAYER2.displayResult()
                self.PLAYER2.displayDice()

                if ROLLS == 3 and len(self.PLAYER2.DICE) > 2:
                    input(
                        f"{self.PLAYER2.getName()} wasn't able to get all the requirements (Press ENTER to continue)")

                while ROLLS < 3 and len(self.PLAYER2.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    self.PLAYER2.TEMP_SCORE = self.PLAYER2.Points()
                    print(f"Would like to keep {self.PLAYER2.TEMP_SCORE} pieces of gold? (Y/n)")
                    OPTION = input("> ")
                    if OPTION.upper() == "N":
                        self.PLAYER2.TEMP_SCORE = 0
                        self.PLAYER2.POINTS = 0
                        self.PLAYER2.rollDice()
                        self.PLAYER2.displayDice()
                        ROLLS += 1
                    else:
                        print(f"Rolls: {ROLLS}")
                        self.PLAYER2.SCORE = self.PLAYER2.addScore(self.PLAYER2.TEMP_SCORE)
                        input(f"{self.PLAYER2.getName()}'s total amount of booty is {self.PLAYER2.SCORE} (Press ENTER to continue)")
                        break

                if ROLLS == 3 and len(self.PLAYER2.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    if self.PLAYER2.TEMP_SCORE == 0:
                        self.PLAYER2.TEMP_SCORE = self.PLAYER2.Points()
                    self.PLAYER2.SCORE = self.PLAYER2.addScore(self.PLAYER2.TEMP_SCORE)
                    input(
                        f"{self.PLAYER2.getName()}'s total amount of booty is {self.PLAYER2.SCORE} (Press ENTER to continue)")

                self.PLAYER2.reset()

            if self.PLAYER1.SCORE > self.__DEALER.SCORE:
                print("Player 1 Wins!")
            else:
                print("Dealer Wins")
            return Game()

        elif self.CHOICE == 4:
            exit()


if __name__ == "__main__":
    GAME = Game()
    CHOICE = GAME.menu()
    GAME.run()
