# c_engine.py inside ship_captain_crew directory
"""
Title: Game engine
Author: Beatrix Bicomong
Date-created: 29-09-22
"""
from b_player import Player


class Game:
    """
    how the game will function
    """

    def __init__(self):
        """
        creating engine object
        """
        self.__DEALER = Player("Dealer")
        self.PLAYER1 = None
        self.PLAYER2 = None
        self.CHOICE = None

    def setup(self):
        """
        Game title and ship art
        :return: None
        """
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

    def menu(self):
        """
        user menu
        :return: None
        """
        print("""
            1. Rules
            2. One Player (PLY vs PC)
            3. Two Players (PLY1 vs PLY2)
            4. Exit
            """)
        self.CHOICE = int(input("> "))
        return self.CHOICE

    def __int__(self):
        """
        transform CHOICE into int
        :return: int
        """
        return self.CHOICE

    def run(self):
        """
        how main game runs
        :return: None
        """
        if self.CHOICE == 1:
            print("""
 For either single or two players:
 1. When it's the player's turn, they will have only three rolls to get Ship, Captain and Crew in this order
 2. Once the requirements are met, the two remaining dice will be the left over booty.
     - Depending on how many rolls the player has left, if the player gets the required dice before the third roll.
     - The player is able to re-roll their remaining dice to get better booty.
 3. However if the player is not able to get all the required dice within three rolls, their turn ends for the next player.
             """)
            print("Press (Y) to go back to menu")
            BUTTON = input("> ")
            if BUTTON.upper() == "Y":
                return Game()
        elif self.CHOICE == 2:
            # SINGLE PLAYER
            PLAYER_NAME = input("Player Name: ")
            self.PLAYER1 = Player(PLAYER_NAME)
            while self.PLAYER1.isWinner() is False and self.__DEALER.isWinner() is False:
                # --- PLAYER 1 TURN --- #
                # Rolls until all rolls are used or all requirements found
                print(f"{self.PLAYER1.getName()}'s Turn")
                ROLLS = 0
                while ROLLS < 3 and len(self.PLAYER1.DICE) > 2:
                    self.PLAYER1.rollDice()
                    self.PLAYER1.holdDie()
                    ROLLS += 1
                    if ROLLS != 3 and len(self.PLAYER1.DICE) > 2:
                        self.PLAYER1.reroll()

                # Displays dice results and remaining dice
                self.PLAYER1.displayResult()
                self.PLAYER1.displayDice()

                # If player was not able to get all needed dice
                if ROLLS == 3 and len(self.PLAYER1.DICE) > 2:
                    input("You weren't able to get all the requirements (Press ENTER to continue)")

                # If player was able to get all needed dice within three rolls
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

                # Calculates score if all rolls are used
                if ROLLS == 3 and len(self.PLAYER1.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    if self.PLAYER1.TEMP_SCORE == 0:
                        self.PLAYER1.TEMP_SCORE = self.PLAYER1.Points()  # NOTE: for calculating into the final roll NOT from re-rolling
                    self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                    input(f"Your total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")

                # RESET ASSETS
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

                # only displays result
                self.__DEALER.displayResult()

                if ROLLS == 3 and len(self.__DEALER.DICE) > 2:
                    input("Dealer wasn't able to get all the requirements (Press ENTER to continue)")

                while ROLLS < 3 and len(self.__DEALER.DICE) == 2:
                    self.__DEALER.TEMP_SCORE = self.__DEALER.Points()
                    # if dealer has a score higher or equal to five within three rolls, they need to re-roll
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

            # Displays Winner
            if self.PLAYER1.SCORE > self.__DEALER.SCORE:
                print(f"{self.PLAYER1.getName()} Wins!")
            else:
                print("Dealer Wins")
            return Game()

        elif self.CHOICE == 3:
            # TWO PLAYERS - sets players names
            PLAYER_NAME1 = input("Player1 Name: ")
            self.PLAYER1 = Player(PLAYER_NAME1)
            PLAYER_NAME2 = input("Player2 Name: ")
            self.PLAYER2 = Player(PLAYER_NAME2)
            while self.PLAYER1.isWinner() is False and self.PLAYER2.isWinner() is False:
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
                        print(f"Rolls: {ROLLS}")  # Calculates score
                        self.PLAYER1.SCORE = self.PLAYER1.addScore(self.PLAYER1.TEMP_SCORE)
                        input(
                            f"{self.PLAYER1.getName()}'s total amount of booty is {self.PLAYER1.SCORE} (Press ENTER to continue)")
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
                        input(
                            f"{self.PLAYER2.getName()}'s total amount of booty is {self.PLAYER2.SCORE} (Press ENTER to continue)")
                        break

                if ROLLS == 3 and len(self.PLAYER2.DICE) == 2:
                    print(f"Rolls: {ROLLS}")
                    if self.PLAYER2.TEMP_SCORE == 0:
                        self.PLAYER2.TEMP_SCORE = self.PLAYER2.Points()
                    self.PLAYER2.SCORE = self.PLAYER2.addScore(self.PLAYER2.TEMP_SCORE)
                    input(
                        f"{self.PLAYER2.getName()}'s total amount of booty is {self.PLAYER2.SCORE} (Press ENTER to continue)")

                self.PLAYER2.reset()

            # Displays Winner
            if self.PLAYER1.SCORE > self.PLAYER2.SCORE:
                print(f"{self.PLAYER1.getName()} Wins!")
            else:
                print(f"{self.PLAYER2.getName()} Wins!")
            return Game()

        elif self.CHOICE == 4:
            exit()
