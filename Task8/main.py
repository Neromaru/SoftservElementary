class Fib:
    def __init__(self, l_limit, r_limit):
        self.left_limit = l_limit
        self.right_limit = r_limit

    def _fib(self):
        a, b = 0, 1
        in_range = list()
        while a <= self.right_limit:
            if self.left_limit <= a <= self.right_limit:
                in_range.append(str(a))
            a, b = b, a + b
        return in_range

    def fib_in_range(self):
        result = self._fib()
        return ','.join(result)


if __name__ == '__main__':
    fib = Fib(1, 55)
    print(fib.fib_in_range())
