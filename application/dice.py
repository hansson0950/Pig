"""Dice class."""
import random


class Dice:
    """Dice class.

    ### Description:
    A class representing a six-sided die.

    ### Methods:
    - roll(): Roll the die and return the result as an
    - integer between 1 and 6.
    """

    def roll(self):
        """Roll the die.

        ### Description:
        This method is produces an integer between 1 and 6.
        It is supposed to mimic a die.

        ### Returns:
        - An integer between 1 and 6 representing the result of the die roll.
        """
        return random.randint(1, 6)
