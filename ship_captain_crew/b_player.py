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

    def __init__(self):
        """
        creating player object
        """
        self.DICE = []
        for i in range(5):
            self.DICE.append(Die())
        self.HELD = []
        self.SCORE = 0
        self.SHIP = True
        self.CAPTAIN = True
        self.CREW = True

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
        print("Dice")
        for die in self.DICE:
            die.displayDie()

        if self.SHIP is True:
            for i in range(len(self.DICE)):
                if self.DICE[i].DIE_NUM == 6:
                    self.SHIP = False
                    print(f"Found Ship {self.DICE[i].DIE_NUM}")
                    self.HELD.append(self.DICE.pop(i))
                    break
        if len(self.HELD) == 0:
            print("No Ship found")

        if self.CAPTAIN is True:
            for i in range(len(self.DICE)):
                if self.DICE[i].DIE_NUM == 5
                if self.DICE[i].DIE_NUM == 5:
                    print(f"Found Captain {self.DICE[i].DIE_NUM}")
                    if self.SHIP is False:
                        self.CAPTAIN = False
                        self.HELD.append(self.DICE.pop(i))
                        break
        if len(self.HELD) == 1:
            print("No Captain found")

        if self.CREW is True:
            for i in range(len(self.DICE)):
                if self.DICE[i].DIE_NUM == 4:
                    print(f"Found Crew {self.DICE[i].DIE_NUM}")
                    if self.CAPTAIN is False:
                        self.CREW = False
                        self.HELD.append(self.DICE.pop(i))
                        break
        if len(self.HELD) == 2:
            print("No Crew found")

        print("Remaining Dice:")
        for die in self.DICE:
            die.displayDie()




if __name__ == "__main__":
    NAME = Player()
    NAME.rollDice()
    NAME.holdDie()
