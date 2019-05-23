import unittest

from Task3.main import TriangleBank


class TestTriangleBank(unittest.TestCase):

    def test_normalize_string(self):
        initial = TriangleBank()
        initial_data = "    Triangle 1"
        expected = "triangle1"
        return self.assertEqual(initial.normalize_string(initial_data),
                                expected)

    def test_square_by_geron(self):
        initial = TriangleBank()
        initial_data = (3, 4, 5)
        expected = 6
        return self.assertEqual(initial.geron(*initial_data),
                                expected)

    def test_read_from_csv_input(self):
        initial = TriangleBank()
        initial_data = "Triangle1, 3, 4, 5"
        expected = ["Triangle1", " 3", " 4", " 5"]
        self.assertEqual(initial.read_from_csv_input(initial_data),
                         expected)

    def test_existence_of_triangle(self):
        initial = TriangleBank
        initial_data = (3, 4, 5)
        expected = True
        return self.assertEqual(initial.triangle_exists(*initial_data),
                                expected)

    def test_triangle_does_not_exists(self):
        initial = TriangleBank
        initial_data = (1, 4, 5)
        expected = False
        return self.assertEqual(initial.triangle_exists(*initial_data),
                                expected)
