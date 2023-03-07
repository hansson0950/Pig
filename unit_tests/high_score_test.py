"""A class for testing the HighScore class."""
import os
import tempfile
import unittest
from unittest.mock import mock_open, patch, call

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from high_score import HighScore # noqa


class TestHighScore(unittest.TestCase):
    """A class for testing the HighScore class."""

    def setUp(self):
        """Create a temporary file and HighScore instance for each test."""
        self.temp_file = tempfile.NamedTemporaryFile()
        self.filename = self.temp_file.name
        self.high_score = HighScore()

    def tearDown(self):
        """Delete the temporary file after each test."""
        os.remove(self.filename)

    def test_load_scores(self):
        """Test loading scores from a file."""
        with patch('builtins.open', mock_open(read_data="Jon: 4\nAl: 6\nTy: 7\n")):
            self.high_score.load_scores('test_filename.txt')
            self.assertEqual(self.high_score.scores, ["Jon: 4\n", "Al: 6\n", "Ty: 7\n"])

    def test_save_scores(self):
        """Test saving scores to a file."""
        self.high_score.scores = ["Jon: 4", "Al: 6", "Ty: 7"]

        with patch("builtins.open", mock_open()) as m:
            self.high_score.save_scores("test_filename.txt")

            m.assert_called_once_with("test_filename.txt", "w")

            handle = m()
            handle.write.assert_has_calls([
                call("Jon: 4\n"), 
                call("Al: 6\n"), 
                call("Ty: 7\n")
            ])

    def test_is_high_score(self):
        """Test checking if a score is a high score."""
        self.high_score.scores = ["Jon: 4", "Al: 6", "Ty: 7"]

        self.high_score.is_high_score(9, "Bosse")
        expected_scores = ["Jon: 4", "Al: 6", "Ty: 7", "Bosse: 9"]
        self.assertEqual(self.high_score.scores, expected_scores)

    def test_get_high_scores(self):
        """Test getting high scores."""
        self.high_score.scores = ["Jon: 4", "Al: 6", "Ty: 7"]
        self.assertListEqual(self.high_score.get_high_scores(),
                             ["Jon: 4", "Al: 6", "Ty: 7"])


if __name__ == "__main__":
    unittest.main()
