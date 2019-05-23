UNITS = {
    0: {
        0: "", 1: "Один", 2: "Два", 3: "Три", 4: "Четыре",
        5: "Пять", 6: "Шесть", 7: "Семь", 8: "Восемь", 9: "Девять"
        },

    'tens': {
        10: "Десять", 11: "Одинадцать", 12: "Двенадцать",
        13: "Тринадцать", 14: "Четырнадцать", 15: "Пятнадцать",
        16: "Шестнадцать", 17: "Семнадцать", 18: "Восемнадцать",
        19: "Девятнадцать"
        },

    1: {
        0: "", 2: "Двадцать", 3: "Тридцать", 4: "Сорок",
        5: "Пятьдесять", 6: "Шестьдесят", 7: "Семдесят",
        8: "Восемдесять", 9: "Девяносто"
        },

    2: {
        0: "", 1: "Сто", 2: "Двести", 3: "Триста", 4: "Четыреста",
        5: "Пятьсот", 6: "Шестьсот", 7: "Семьсот",
        8: "Восемьсот", 9: "Девятьсот"
        }
    }

ADDITIONS = {
    0: " ",
    1: ' Тысяч',
    2: " Милион",
    3: " Милиард"
    }


class NumToWords:

    def __init__(self, number):
        self.number = number
        self.decades = []

    def _split_by_3(self):
        self.decades = [self.number[i:i + 3]
                        for i in range(0, len(self.number), 3)]

    @staticmethod
    def _proceed_tens(two_digits):
        if two_digits == '':
            return ''
        number = int(two_digits)
        if UNITS['tens'].get(number, False):
            return UNITS['tens'].get(number)
        else:
            raw_list = [UNITS[i].get(int(num))
                        for i, num in enumerate(two_digits)]
            return ' '.join(raw_list[::-1])

    def _proceed_hundreds(self, three_digits):
        number = three_digits[::-1]
        hundred = int(number[0])
        tens = number[1:]
        return "{h} {t}".format(h=UNITS[2].get(hundred),
                                t=self._proceed_tens(tens[::-1]))

    @staticmethod
    def _proceed_addition(last_d, hundreds, addition):
        if last_d == 1 and addition != ADDITIONS[0]:
            return "{h}{add}a".format(h=hundreds, add=addition)
        elif 1 < last_d < 5 and addition != ADDITIONS[0]:
            if addition != ADDITIONS[1]:
                return "{h}{add}a".format(h=hundreds, add=addition)
            return "{h}{add}и".format(h=hundreds, add=addition)
        else:
            return "{h}{add}".format(h=hundreds, add=addition)

    def _proceed_thousands(self, thousands, addition):
        last_d = int(thousands[0])
        if len(thousands) == 3:
            hundreds = self._proceed_hundreds(thousands)
        else:
            hundreds = self._proceed_tens(thousands)
        return self._proceed_addition(last_d, hundreds, addition)

    def to_word(self):
        self.number = self.number[::-1]
        self._split_by_3()
        result = []
        for order, numbers in enumerate(self.decades):
            result.append(
                self._proceed_thousands(
                    numbers, ADDITIONS.get(
                        order)
                    )
                )
        return ' '.join(result[::-1])


if __name__ == '__main__':
    new_one = NumToWords('1234567')
    print(new_one.to_word())
