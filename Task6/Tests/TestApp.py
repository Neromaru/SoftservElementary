import unittest

from Task6.app import LuckyTickets


class LuckyTicketsTest(unittest.TestCase):

    def test_passing_invalid_params_to_class(self):
        initila = LuckyTickets(path='Test', mode='NOCHOISE')
        expected = ValueError
        with self.assertRaises(expected):
            initila.run_mode()

    def test_number_of_piter_lucky_tickets_in_test_file(self):
        initila = LuckyTickets(path='Test', mode='piter')
        expected = 3
        return self.assertEqual(initila.run_mode(),
                                expected
                                )

    def test_number_of_moscow_tickets_in_test_file(self):
        initila = LuckyTickets(path='Test', mode='moscow')
        expected = 4
        return self.assertEqual(initila.run_mode(),
                                expected
                                )

    def test_moscow(self):
        initial = LuckyTickets()
        expected = 1
        return self.assertEqual(
            initial.moscow('1111111'),
            expected
            )

    def test_piter(self):
        initial = LuckyTickets()
        expected = 1
        return self.assertEqual(
            initial.piter('1111111'),
            expected
            )
