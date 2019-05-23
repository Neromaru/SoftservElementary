import unittest

from Task8.main import Fib


class TestFib(unittest.TestCase):

    def test_fib_seq_in_range_of_val(self):
        initial = Fib(1, 55)
        expected = '1,1,2,3,5,8,13,21,34,55'
        return self.assertEqual(initial.fib_in_range(),
                                expected)

    def test_fib_seq_in_range_of_val_fail(self):
        initial = Fib(1, 55)
        expected = '1,1,2,3,5,8,13,21,34'
        return self.assertNotEqual(initial.fib_in_range(),
                                   expected)
