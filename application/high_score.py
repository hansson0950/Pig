"""High score class."""
from pathlib import Path


class HighScore:
    """High score class.

    ### Description:
    This class manages the high scores.
    When the program is started, it creates a high_score.txt file
    if it doesn't already exist.
    It will load all high scores when the application starts.
    After a game is finished, it will check if it contained a new high score.
    When the application is shut down, the new scores will be printed
    to the high_scores.txt file.

    ### Attributes:
    - scores (list): A list of high scores.

    ### Methods:
    - create_file(): Create the high_score.txt file if it doesn't
      already exist.
    - load_scores(filename): Load scores from txt file to local list.
    - save_scores(filename): Save scores from local list to txt file.
    - is_high_score(new_score, name): Compare new score to current high
      scores.
    - get_high_scores(): Return list of scores.
    """

    def __init__(self):
        """Initialize list of high scores.

        ### Description:
        Initializes a new instance of the `HighScore` class,
        and initializes its attributes.

        ### Attributes:
        - scores (list): A list of high scores.
        """
        self.scores = []

    def create_file(self):
        """Create the high_score.txt file if it doesn't already exist."""
        file = Path("high_scores.txt")
        file.touch(exist_ok=True)

    def load_scores(self, filename):
        """Load scores.

        ### Description:
        Load the scores from the high_scores.txt
        fie and save it to a local list.

        ### Args:
        - filename (str): The name of the file to load scores from.
        """
        with open(filename, "r", encoding="utf8") as file:
            self.scores = file.read().splitlines()

    def save_scores(self, filename):
        """Save scores.

        ### Description:
        Save scores from local list to the high_scores.txt file.

        ### Args:
        - filename (str): The name of the file to save scores to.
        """
        with open(filename, "w", encoding="utf8") as file:
            for string in self.scores:
                file.write(string + "\n")

    def is_high_score(self, new_score, name):
        """Check high score.

        ### Description:
        Compare the new score of a finished game to the current high scores.
        It starts by adding the name of the player as well as their score to
        the local list. After that, it splits the string that consists of the
        player's name and their score and keeps the score. It will then put the
        scores in the correct order. When all of that is done, a check is made
        to see if the list contains more than five entries. If it does, it
        will remove the sixth entry to keep the high scores at five.

        ### Args:
        - new_score (str): The number of turns it took for the player to reach
        100 points.
        - name (str): The name of the player who won.
        """
        self.scores.append(f"{name}: {new_score}")
        self.scores = sorted(self.scores, key=lambda x: int(x.split(": ")[-1]))
        if len(self.scores > 5):
            self.scores.pop()

    def get_high_scores(self):
        """Get scores.

        ### Description:
        Returns the local list of high scores.

        ### Returns:
        - scores (list): The local list of high scores.
        """
        return self.scores
