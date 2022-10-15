# a_dice.py inside ship_captain_crew directory
"""
Title: Dice class
Author: Beatrix Bicomong
Date-created: 13-10-2022
"""

from random import randint


class Die:
    """
    create a die to roll for random numbers
    """

    # input
    def __init__(self, SIDES=6):
        """
        construct a die
        :param SIDES: int
        """
        self.DIE_MAX = SIDES
        self.DIE_NUM = None

    # processing
    def rollDie(self):
        """
        update die with new number
        :return: None
        """
        self.DIE_NUM = randint(1, self.DIE_MAX)

    # output
    def displayDie(self):
        """
        print the number
        :return: None
        """
        print(self.DIE_NUM)
