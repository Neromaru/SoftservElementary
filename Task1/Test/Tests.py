import unittest

from Task1.main import ChessDesk


class TestChessDesk(unittest.TestCase):

    def test_check_if_desk_valid(self):
        initial = ChessDesk(7, 5)
        expected = True
        return self.assertEqual(initial.check_if_desk_valid(), expected)

    def test_check_if_desk_is_not_valid(self):
        initial = ChessDesk(1, 1)
        expected = ValueError
        with self.assertRaises(expected):
            initial.check_if_desk_valid()

    def test_if_desk_draw(self):
        initial = ChessDesk(4, 4)
        expected = "* * \n * *\n* * \n * *\n"
        return self.assertEqual(initial.draw(), expected)
