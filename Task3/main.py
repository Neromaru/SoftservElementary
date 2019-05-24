from math import sqrt

NOT_EXISTS = 0

class TriangleBank:

    def __init__(self):
        self.bank = {}

    @staticmethod
    def normalize_string(string):
        lower = string.lower()
        no_spaces = lower.replace(' ', '')
        no_tabs = no_spaces.replace('   ', '')
        return no_tabs

    @staticmethod
    def _geron(side_a, side_b, side_c):
        half_perim = (side_a + side_b + side_c)/2
        square = sqrt(
            half_perim
            * (half_perim - side_a)
            * (half_perim - side_b)
            * (half_perim - side_c)
            )
        return square

    @staticmethod
    def read_from_csv_input(prompt):
        return [value.strip() for value in prompt.split(',')]

    @staticmethod
    def triangle_exists(side_1, side_2, side_3):
        side_a, side_b, side_c = float(side_1), float(side_2), float(side_3)
        if side_a == NOT_EXISTS or side_b == NOT_EXISTS \
                or side_c == NOT_EXISTS:
            return False
        elif side_a + side_b <= side_c \
                or side_a + side_c <= side_b \
                or side_c + side_b <= side_a:
            return False
        return True

    def _proceed_and_add_to_bank(self, name, side_a, side_b, side_c):
        key = self.normalize_string(name)
        square = self._geron(float(side_a), float(side_b), float(side_c))
        if self.bank.get(key):
            self.bank[key]['square'] = square
        else:
            self.bank[key] = {'name': name, 'square': square}
        return self

    def _sort_and_represent_bank(self,):
        sorted_list_to_repr = sorted(self.bank.values(),
                                     key=lambda v: v['square']
                                     )
        body = ""
        for num, val in enumerate(sorted_list_to_repr):
            body += "{num}. [{name}]: {val} cm\n"\
                .format(num=num+1, name=val['name'], val=val['square'])
        return body

    def represent_results(self):
        dashes = '='*13
        header = "{dashes} Triangle list: {dashes}\n".format(dashes=dashes)
        body = self._sort_and_represent_bank()
        return "{head}{body}".format(head=header, body=body)

    def run(self):
        while True:
            csv = input("Input data of a triangle via csv format:\n")
            data = self.read_from_csv_input(csv)
            name, side_a, side_b, side_c = data
            if self.triangle_exists(side_a, side_b, side_c):
                self._proceed_and_add_to_bank(name, side_a, side_b, side_c)
            else:
                print("This triangle doesn't exists try another one")
            continuation = input("Would you like to continue?\n")
            if continuation.lower() not in ['y', 'yes']:
                print(self.represent_results())
                break


def main():
    bank = TriangleBank()
    bank.run()


if __name__ == '__main__':
    main()


class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class Student:
    def __init__(self, name, surname, second_name, session_mark):
        self.name = name
        self.surname = surname
        self.second_name = second_name
        self.session = session_mark

    def has_grant(self, avg_mark):
        if self.session > avg_mark:
            return True
        return False

