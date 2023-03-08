"""Computer class."""
from player import Player


class ComputerPlayer(Player):
    """Computer player.

    ### Description
        A computer player class that inherits from the Player class.

    ### Attributes:
        Inherits all attributes from Player class.

    ### Methods:
        __init__():
            Initializes the computer player by calling the constructor of the
            Player class.

        choose_move():
            Determines whether the computer player should roll or hold based
            on the current game state.

    """

    def __init__(self):
        """Initialize computer player."""
        super().__init__("Computer")

    def choose_move(self):
        """Choose move for computer.

        ### Description
            Determines whether the computer player should roll or hold based on
            the current game state.

        ### Returns:
            String indicating whether the computer player should roll or hold.
                - "roll": if the turn score is less than 20 or if the total
                  score after adding the turn score is less than 100.

                - "hold": if the turn score is greater than or equal to 20 or
                  if the total score after adding the turn score is greater
                  than or equal to 100.

        """
        if self.turn_score >= 20 or self.turn_score + self.score >= 100:
            return "hold"
        return "roll"
