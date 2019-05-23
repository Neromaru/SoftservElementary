import unittest

from Task7.main import NaturalOrder


class TestNaturalOrder(unittest.TestCase):

    def test_root_as_a_border_value(self):
        initial = NaturalOrder(64)
        expected = 8
        return self.assertEqual(
            initial.check_rot(64**0.5),
            expected
            )

    def test_root_as_float_border_value(self):
        initial = NaturalOrder(65)
        expected = 9
        return self.assertEqual(
            initial.check_rot(65**0.5),
            expected
            )

    def test_process_natural_order(self):
        initial = NaturalOrder(65)
        expected = ','.join([str(i) for i in range(1, 9)])
        return self.assertEqual(
            initial.process_natural_order(),
            expected
            )
