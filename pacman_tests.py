import unittest

from pacman import find_pacman


class PacmanTest(unittest.TestCase):

    def test_find_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, 3)
        self.assertEqual(y, 5)
