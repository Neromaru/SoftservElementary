class ChessDesk:
    def __init__(self, width=0, height=0):
        self.width = int(width)
        self.height = int(height)

    def draw(self):
        cell = '* '
        half_width = self.width//2
        half_height = self.height//2
        try:
            self.check_if_desk_valid()
            star_desh = cell*half_width + cell*(half_width % 2)
            desh_star = cell[::-1]*half_width
            return f"{star_desh}\n" \
                   f"{desh_star}\n" * half_height \
                   + f"{star_desh}" * (self.height % 2)
        except ValueError:
            print('You probably want a stick ot nothing')

    def check_if_desk_valid(self):
        if self.width >= 2 and self.height >= 2:
            return True
        else:
            raise ValueError

    def __call__(self, width=0, height=0):
        self.width = width
        self.height = height


if __name__ == '__main__':
    desk = ChessDesk(4, 4)
    print(desk.draw())
