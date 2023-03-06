"""Computer class."""
from player import Player


class ComputerPlayer(Player):
    """Computer class."""

    def __init__(self):
        """Initialize computer player."""
        super().__init__("Computer")

    def choose_move(self):
        """Choose whether to roll or hold."""
        if self.turn_score >= 20 or self.turn_score + self.score >= 100:
            return "hold"
        return "roll"
