"""Dice class."""
import random


class Dice:
    """Dice class."""

    def roll(self):
        """Roll the die."""
        return random.randint(1, 6)
