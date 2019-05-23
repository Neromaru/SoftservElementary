import unittest

from Task5.main import NumToWords


class TestNumToWords(unittest.TestCase):

    def test_to_words(self):
        initial = NumToWords('123')
        expected = "Сто Двадцать Три "
        return self.assertEqual(
                initial.to_word(), expected
               )
