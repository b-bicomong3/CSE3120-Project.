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
        self.TEMP_SCORE = 0
        self.SHIP = False
        self.CAPTAIN = False
        self.CREW = False
        self.FOUND = False
        self.FOUND_1 = False
        self.FOUND_2 = False
        self.__NAME = NAME

    def Score(self):
        """

        :return:
        """
        self.TEMP_SCORE = 0
        for i in range(2):
            self.TEMP_SCORE += self.DICE[i].DIE_NUM
        return self.TEMP_SCORE

    def addScore(self, POINTS):
        """

        :return:
        """
        self.SCORE += POINTS
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
            print(f"Found Ship")
        else:
            print("Ship not found")

        for i in range(len(self.DICE) - 1, -1, -1):
            if self.DICE[i].DIE_NUM == 5:
                self.FOUND_1 = True
                if self.SHIP is True and self.CAPTAIN is False:
                    self.HELD.append(self.DICE.pop(i))
                    self.CAPTAIN = True
        if self.FOUND_1 is True:
            print(f"Found Captain")
        else:
            print("Captain not found")

        for i in range(len(self.DICE) - 1, -1, -1):
            if self.DICE[i].DIE_NUM == 4:
                self.FOUND_2 = True
                if self.CAPTAIN is True and self.CREW is False:
                    self.HELD.append(self.DICE.pop(i))
                    self.CREW = True
        if self.FOUND_2 is True:
            print(f"Found Crew")
        else:
            print("Crew not found")

        if len(self.HELD) == 3:
            print("Remaining Dice:")
            for die in self.DICE:
                die.displayDie()

    def resetDie(self):
        """
        move all dice from HELD to DICE
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

    def reroll(self):
        if self.FOUND_1 is False:
            self.FOUND_2 = False
        elif self.FOUND is False:
            self.FOUND_1 = False

    def getName(self):
        return self.__NAME

    def isWinner(self):
        if self.SCORE >= 20:
            return True
        else:
            return False


# If __name__ == "__main__":
#    NAME = Player()
#
#    for i in range(2):
#        NAME.rollDice()
#        NAME.holdDie()
#        NAME.reroll()
