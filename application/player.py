"""Player class."""
from dice import Dice
from ui import UI


class Player:
    """Player class."""

    def __init__(self, name):
        """Initialize the player."""
        self.name = name
        self.turn_score = 0
        self.total_turns = 0
        self.score = 0
        self.dice = Dice()
        self.ui = UI()  # pylint: disable-msg=C0103

    def roll_dice(self):
        """Roll the die."""
        roll = self.dice.roll()
        self.ui.display_roll(roll)
        return roll

    def add_to_score(self, points):
        """Add points to score."""
        self.score = points
        return self.score

    def add_to_turn(self, points):
        """Add points to current turn."""
        self.turn_score += points

    def end_turn(self):
        """End current turn."""
        self.ui.display_turn_end(self.name)
