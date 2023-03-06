"""A class for testing the HighScore class."""
import os
import tempfile
import unittest

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from high_score import HighScore # noqa


class TestHighScore(unittest.TestCase):
    """A class for testing the HighScore class."""

    def setUp(self):
        """Create a temporary file and HighScore instance for each test."""
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.filename = self.temp_file.name
        self.high_score = HighScore(filename=self.filename)

    def tearDown(self):
        """Delete the temporary file after each test."""
        os.remove(self.filename)

    def test_load_scores(self):
        """Test loading scores from a file."""
        self.high_score.scores = []
        self.high_score.load_scores()
        self.assertListEqual(self.high_score.scores, [])

        with open(self.filename, "w") as file:
            file.write("Jon: 4 turns\nAl: 6 turns\nTy: 7 turns\n")

        self.high_score.load_scores()
        self.assertListEqual(self.high_score.scores, ["Jon: 4 turns",
                                                      "Al: 6 turns",
                                                      "Ty: 7 turns"])

    def test_save_scores(self):
        """Test saving scores to a file."""
        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "")

        self.high_score.scores = ["Jon: 4 turns", "Al: 6 turns", "Ty: 7 turns"]
        self.high_score.save_scores()

        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "4\n6\n7\n")

    def test_is_high_score(self):
        """Test checking if a score is a high score."""
        self.high_score.scores = [4, 6, 7]

        self.assertTrue(self.high_score.is_high_score(9))
        self.assertTrue(self.high_score.is_high_score(2))
        self.assertFalse(self.high_score.is_high_score(5))
        self.assertFalse(self.high_score.is_high_score(6))

    def test_get_high_scores(self):
        """Test getting high scores"""
        self.high_score.scores = [4, 6, 7]
        self.assertListEqual(self.high_score.get_high_scores(),
                             [4, 6, 7])


if __name__ == "__main__":
    unittest.main()
