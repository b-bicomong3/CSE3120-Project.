# b_player.py inside ship_captain_crew directory
"""
Title: PLayer class
Author: Beatrix Bicomong
Date-created: 13-10-2022
"""

from a_dice import Die


class Player:
    """
    the player from the game Ship, Captain and Crew
    """

    def __init__(self, NAME):
        """
        creating player object
        """
        self.DICE = []
        for i in range(5):
            self.DICE.append(Die())
        self.HELD = []
        self.SCORE = 0
        self.POINTS = 0
        self.TEMP_SCORE = 0
        self.SHIP_DICE = 0
        self.CAPTAIN_DICE = 0
        self.CREW_DICE = 0
        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False
        self.FOUND = False
        self.FOUND_1 = False
        self.FOUND_2 = False
        self.__NAME = NAME

    # MODIFIER METHODS

    # INPUTS
    def points(self):
        """
        calculates the amount of gold based on the die number
        :return: int
        """
        for i in range(len(self.DICE)):
            self.POINTS += self.DICE[i].DIE_NUM
        return self.POINTS

    def addScore(self, POINTS):
        """
        adds points to score
        :param POINTS: int
        :return: int
        """
        self.SCORE += self.POINTS
        return self.SCORE

    # PROCESSING

    def rollDice(self):
        """
        rolls dice
        :return: None
        """
        for die in self.DICE:
            die.rollDie()

    def holdDie(self):
        """
         automatically hold die for player
         :return: None
         """
        for i in range(len(self.DICE) - 1, -1, -1):
            if self.DICE[i].DIE_NUM == 6:
                self.FOUND = True
                if self.SHIP is False:
                    self.HELD.append(self.DICE.pop(i))
                    self.SHIP = True
        if self.FOUND is True:
            self.SHIP_DICE = 1

        for i in range(len(self.DICE) - 1, -1, -1):
            if self.DICE[i].DIE_NUM == 5:
                self.FOUND_1 = True
                if self.SHIP is True and self.CAPTAIN is False:
                    self.HELD.append(self.DICE.pop(i))
                    self.CAPTAIN = True
        if self.FOUND_1 is True:
            self.CAPTAIN_DICE = 1

        for i in range(len(self.DICE) - 1, -1, -1):
            if self.DICE[i].DIE_NUM == 4:
                self.FOUND_2 = True
                if self.CAPTAIN is True and self.CREW is False:
                    self.HELD.append(self.DICE.pop(i))
                    self.CREW = True
        if self.FOUND_2 is True:
            self.CREW_DICE = 1

    def reset(self):
        """
        move all dice from HELD to DICE, true and false statements and temporary score
        :return: None
        """
        self.DICE += self.HELD
        self.HELD = []
        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False
        self.FOUND = False
        self.FOUND_1 = False
        self.FOUND_2 = False
        self.TEMP_SCORE = 0
        self.POINTS = 0
        self.SHIP_DICE = 0
        self.CAPTAIN_DICE = 0
        self.CREW_DICE = 0

    def reroll(self):
        """
        restarts requirement statements
        :return: None
        """
        if self.FOUND_1 is False:
            self.FOUND_2 = False
            self.CREW_DICE = 0
        elif self.FOUND is False:
            self.FOUND_1 = False
            self.CAPTAIN_DICE = 0

    # OUTPUTS

    def displayResult(self):
        """
        displays whether a required dice was found or not
        :return: None
        """
        if self.SHIP_DICE == 0:
            print("Ship was not found")
        else:
            print("Ship was found")
        if self.CAPTAIN_DICE == 0:
            print("Captain was not found")
        else:
            print("Captain was found")
        if self.CREW_DICE == 0:
            print("Crew was not found")
        else:
            print("Crew was found")

    def displayDice(self):
        """
        displays the remaining dice that calculates the player's score
        :return:
        """
        if len(self.HELD) == 3:
            print("Remaining Dice:")
            for die in self.DICE:
                die.displayDie()

    # ACCESSOR METHODS

    def getName(self):
        """
        get player's name
        :return: str
        """
        return self.__NAME

    def isWinner(self):
        """
        dictates winner
        :return: bool
        """
        if self.SCORE >= 20:
            return True
        else:
            return False
