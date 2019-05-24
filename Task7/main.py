from math import sqrt


class NaturalOrder:
    def __init__(self, number):
        self.number = number

    def _validate_number(self):
        if self.number <= 0:
            return False
        return True

    @staticmethod
    def check_rot(root):
        if root == int(root):
            return int(root)
        else:
            return int(root)+1

    def process_natural_order(self):
        if not self._validate_number():
            return None
        root = sqrt(self.number)
        order_n = range(1, self.check_rot(root))
        return ','.join(order_n)


if __name__ == '__main__':
    order = NaturalOrder(65)
    print(order.process_natural_order())
