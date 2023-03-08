"""Dice class."""
import random


class Dice:
    """A class representing a six-sided die.

    Attributes:
        None

    Methods:
        roll(): Roll the die and return the result as an
        integer between 1 and 6.

    """

    def roll(self):
        """Roll the die.

        Returns:
            An integer between 1 and 6 representing the result of the die roll.
        """
        return random.randint(1, 6)
