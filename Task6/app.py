import os
from string import punctuation


class LuckyTickets:

    def __init__(self, path='', mode=''):
        self.path = path
        self.mode = mode
        self.score = 0

    def _validate_path(self):
        if os.path.isfile(self.path) and os.path.exists(self.path):
            return True
        else:
            raise ValueError("Path doesn't lead to file or not exists")

    @staticmethod
    def _validate_line(line):
        if punctuation in line or len(line) != 6 or not isinstance(line, str):
            raise ValueError('Line should have only 1 ticker without any '
                             'punctuaction')
        return True

    def read_file_by_line(self, function):
        self._validate_path()
        with open(self.path, 'r') as lucky_list:
            for line in lucky_list:
                self._validate_line(line.rstrip())
                self.score += function(line.rstrip())

    @staticmethod
    def moscow(ticket):
        ticket_half = len(ticket)//2
        first_half = sum(map(lambda x: int(x), ticket[:ticket_half]))
        second_half = sum(map(lambda x: int(x), ticket[ticket_half:]))
        if first_half == second_half:
            return 1
        else:
            return 0

    @staticmethod
    def piter(ticket):
        even_sum = sum(map(lambda x: int(x), ticket[0::2]))
        odd_sum = sum(map(lambda x: int(x), ticket[1::2]))
        if even_sum == odd_sum:
            return 1
        else:
            return 0

    def run_mode(self):
        if self.mode == 'Moscow' or self.mode == 'moscow':
            self.read_file_by_line(self.moscow)
            return self.score
        elif self.mode == 'Piter' or self.mode == 'piter':
            self.read_file_by_line(self.piter)
            return self.score
        else:
            raise ValueError('None of fit parameters were passed')


def main():
    exiting = False
    while not exiting:
        lucky = LuckyTickets()
        path_to_file = input('Please provide a path to file with Lucky '
                             'Tickets\n')
        mode = input('Please select one of the modes for tickets\n')
        lucky.path = path_to_file
        lucky.mode = mode
        print("There are : {number} lucky tickets".format(
            number=lucky.run_mode()))
        confirm = input('Would you like to continue ?\n[Y/y]\n')
        if confirm not in ['Y', 'y']:
            exiting = True
        else:
            lucky.score = 0


if __name__ == '__main__':
    main()
