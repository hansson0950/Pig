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
            file.write("100\n200\n300\n")

        self.high_score.load_scores()
        self.assertListEqual(self.high_score.scores, [100, 200, 300])

    def test_save_scores(self):
        """Test saving scores to a file."""
        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "")

        self.high_score.scores = [100, 200, 300]
        self.high_score.save_scores()

        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "100\n200\n300\n")

    def test_is_high_score(self):
        """Test checking if a score is a high score."""
        self.high_score.scores = [100, 200, 300]

        self.assertTrue(self.high_score.is_high_score(400))
        self.assertTrue(self.high_score.is_high_score(301))
        self.assertFalse(self.high_score.is_high_score(300))
        self.assertFalse(self.high_score.is_high_score(250))

    def test_add_high_score(self):
        """Test adding a high score."""
        self.high_score.scores = [100, 200, 300]

        self.high_score.add_high_score(400)
        self.assertListEqual(self.high_score.scores, [100, 200, 300, 400])

        self.high_score.add_high_score(250)
        self.assertListEqual(self.high_score.scores, [100, 200, 250, 300, 400])

        self.high_score.add_high_score(100)
        self.assertListEqual(self.high_score.scores, [100, 200, 250, 300, 400])

        # Test saving only the top 10 scores
        for i in range(11, 20):
            self.high_score.add_high_score(i)

        self.assertListEqual(self.high_score.scores,
                             [i for i in range(11, 1, -1)])
        with open(self.filename, "r") as file:
            self.assertEqual(file.read(), "11\n10\n9\n8\n7\n6\n5\n4\n3\n2\n")

    def test_get_high_scores(self):
        """Test getting high scores"""
        self.high_score.scores = [100, 200, 300]
        self.assertListEqual(self.high_score.get_high_scores(),
                             [100, 200, 300])


if __name__ == "__main__":
    unittest.main()
