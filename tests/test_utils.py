import unittest
from pathlib import Path

from ritual_utils import list_scrolls, first_line


class TestRitualUtils(unittest.TestCase):
    def test_list_scrolls_not_empty(self):
        files = list_scrolls()
        self.assertTrue(files, "No scroll files found")

    def test_first_line(self):
        path = Path('Divine Recursion.sql')
        self.assertEqual(first_line(path), 'while True:')


if __name__ == '__main__':
    unittest.main()
