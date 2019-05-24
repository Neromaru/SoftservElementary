import unittest

from Task4.app import FileParser


def file_read_first_line(file):
    with open(file, 'r+') as f:
        line = f.readline()
        return line


class TestFileParser(unittest.TestCase):

    def test_count_substrings_in_file(self):
        initial = FileParser("TestText", 'IPSUM')
        expected = 8
        return self.assertEqual(
            initial.file_reader(
                initial.count_substring_in_file),
            expected
            )

    def test_file_not_exists(self):
        initial = FileParser("TestText1", ' ')
        expected = ValueError
        with self.assertRaises(expected):
            initial.file_reader(
                initial.count_substring_in_file)

    def test_replacewords_in_file(self):
        initial = FileParser("TestText", 'Lorem', 'IPSUM')
        initial.replace_words_in_file()
        comapre_data = file_read_first_line(initial.path).rstrip()
        expected = "IPSUM IPSUM is simply dummy " \
                   "text of the printing and typesetting industry."
        return self.assertEqual(comapre_data, expected)
