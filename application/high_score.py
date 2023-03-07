"""High score class."""


class HighScore:
    """High score class."""

    def __init__(self):
        """Initialize list of high scores."""
        self.scores = []

    def load_scores(self, filename):
        """Load scores from txt file to local list."""
        with open(filename, "r") as file:
            self.scores = file.readlines()

    def save_scores(self, filename):
        """Save scores from local list to txt file."""
        with open(filename, "w") as file:
            for string in self.scores:
                file.write(string + "\n")

    def is_high_score(self, new_score, name):
        """Compare new score to current high scores."""
        # if len(self.scores) == 0:
        #     self.scores.append(f"{name}: {new_score} turns")

        # current_index = 0
        # for string in self.scores:
        #     index1 = string.rfind(":") + 2
        #     index2 = string.rfind(" ")
        #     score = int(string[index1:index2])

        #     if new_score > score:
        #         current_index += 1
        #         continue
        #     new_entry = f"{name}: {new_score} turns"
        #     self.scores.insert(current_index, new_entry)

        #     if len(self.scores) > 5:
        #         self.scores.pop()
        #     break
        self.scores.append(f"{name}: {new_score}")
        self.scores = sorted(self.scores, key=lambda x: int(x.split(": ")[-1]))

    def get_high_scores(self):
        """Return list of scores."""
        return self.scores
