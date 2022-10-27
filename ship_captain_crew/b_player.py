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

    def Points(self):
        """

        :return:
        """
        for i in range(len(self.DICE)):
            self.POINTS += self.DICE[i].DIE_NUM
        return self.POINTS

    def addScore(self, POINTS):
        """

        :return:
        """
        self.SCORE += self.POINTS
        return self.SCORE

    def rollDice(self):
        """
        rolls dice
        :return:
        """
        for die in self.DICE:
            die.rollDie()

    def holdDie(self):
        """
         automatically hold die for player
         :return:
         """
        #        print("Dice")
        #        for die in self.DICE:
        #            die.displayDie()

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
        if self.FOUND_1 is False:
            self.FOUND_2 = False
            self.CREW_DICE = 0
        elif self.FOUND is False:
            self.FOUND_1 = False
            self.CAPTAIN_DICE = 0

    def getName(self):
        return self.__NAME

    def isWinner(self):
        if self.SCORE >= 20:
            return True
        else:
            return False

    def displayResult(self):
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
        if len(self.HELD) == 3:
            print("Remaining Dice:")
            for die in self.DICE:
                die.displayDie()

# If __name__ == "__main__":
#    NAME = Player()
#
#    for i in range(2):
#        NAME.rollDice()
#        NAME.holdDie()
#        NAME.reroll()
