"""High score class."""
from pathlib import Path


class HighScore:
    """High score class."""

    def __init__(self):
        """Initialize list of high scores."""
        self.scores = []

    def create_file(self):
        """Create the high_score.txt file if it doesn't already exist."""
        file = Path("high_scores.txt")
        file.touch(exist_ok=True)

    def load_scores(self, filename):
        """Load scores from txt file to local list."""
        with open(filename, "r", encoding="utf8") as file:
            self.scores = file.read().splitlines()

    def save_scores(self, filename):
        """Save scores from local list to txt file."""
        with open(filename, "w", encoding="utf8") as file:
            for string in self.scores:
                file.write(string + "\n")

    def is_high_score(self, new_score, name):
        """Compare new score to current high scores."""
        self.scores.append(f"{name}: {new_score}")
        self.scores = sorted(self.scores, key=lambda x: int(x.split(": ")[-1]))

    def get_high_scores(self):
        """Return list of scores."""
        return self.scores
