"""Player class."""
from dice import Dice
from ui import UI


class Player:
    """Represents a player in the game.

    ### Description:
    This class represents a player by creating an object.
    The object stores some valuable information such as the name,
    scores and turns.

    ### Attributes:
    - name (str): The name of the player.
    - turn_score (int): The total score accumulated by the player in the
      current turn.
    - total_turns (int): The total number of turns taken by the player.
    - score (int): The total score of the player.
    - dice (Dice): A Dice object used to roll the dice.
    - ui (UI): A UI object used to display information to the player.

    ### Methods:
    - __init__(self, name: str): Initializes a new Player object with the
      given name.
    - roll_dice(self) -> int: Rolls the dice and returns the result.
    - add_to_score(self, points: int) -> int: Adds the given number of points
      to the player's score and returns the updated score.
    - add_to_turn(self, points: int) -> None: Adds the given number of points
      to the player's turn score.
    - reset_turn_score(self) -> None: Resets the player's turn score to zero.
    - end_turn(self) -> None: Ends the player's current turn and displays a
      message indicating the end of the turn.
    """

    def __init__(self, name):
        """Initialize a new Player.

        ### Description:
        Initializes a new player object with the given name.

        ### Args:
        - name(str): The name of the player.
        """
        self.name = name
        self.turn_score = 0
        self.total_turns = 0
        self.score = 0
        self.dice = Dice()
        self.ui = UI()  # pylint: disable-msg=C0103

    def roll_dice(self):
        """Roll the die.

        ### Description:
        Rolls the die and returns the result.

        ### Returns:
        - int: The result of the dice roll.
        """
        roll = self.dice.roll()
        self.ui.display_roll(roll)
        return roll

    def add_to_score(self, points):
        """Add points to score.

        ### Description:
        This method is called when the player chooses to hold.
        The score of the completed turn will be added to their total score.

        ### Args:
        - points (int): The number of points to add to the player's score.

        ### Returns:
        - int: The updated score of the player.
        """
        self.score += points
        return self.score

    def add_to_turn(self, points):
        """Add points to current turn.

        ### Description:
        After the die is rolled and it lands on something other than one,
        this method will be called. It will add the number of the die to
        the player's current turn score.

        ### Args:
        - points (int): The number of points to add to the player's turn score.
        """
        self.turn_score += points

    def reset_turn_score(self):
        """Reset turn score.

        ### Description:
        Resets the player's current turn score to zero.
        This occurs when the player chooses to hold, or rolls a one.
        """
        self.turn_score = 0

    def end_turn(self):
        """End current turn.

        ### Description:
        Ends the player's current turn.
        This occurs when the player chooses to hold, or rolls a one.
        """
        self.ui.display_turn_end(self.name)
