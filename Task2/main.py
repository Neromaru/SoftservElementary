from math import sqrt, pow


class Envelope:

    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def _sort_values_ascending(self):
        if self.width < self.height:
            self.width, self.height = self.height, self.width
        return self

    def _diagonals(self):
        self.diagonal = sqrt(pow(self.width, 2) + pow(self.height, 2))
        return self

    def _find_sin_to_diag(self):
        self._diagonals()
        self.sin = self.height/self.diagonal
        return self

    def _projection_on_wall_while_rotated(self):
        self._find_sin_to_diag()
        self.projection = self.sin * (self.width + self.height)

    def prepare_envelope_to_pack(self):
        self._projection_on_wall_while_rotated()
        self._sort_values_ascending()
        return self


class EnvelopeComparator:

    def __init__(self, envelope1, envelope2):
        self.envelope1 = envelope1
        self.envelope2 = envelope2

    @staticmethod
    def _compare_projection_to_height(envelope1, envelope2):
        if envelope1.projection < envelope2.height and envelope1.diagonal < \
                envelope2.diagonal:
            return True
        return False

    @staticmethod
    def _gte_envelope(envelope1, envelope2):
        if envelope1.width >= envelope2.width or \
                envelope1.height >= envelope2.height:
            return True
        return False

    def compare_envelopes_to_pack(self):
        self.envelope1.prepare_envelope_to_pack()
        self.envelope2.prepare_envelope_to_pack()
        if self.envelope1.width < self.envelope2.width and \
                self.envelope1.height < self.envelope2.height:
            return "You can pack one envelope in to another"
        elif self._gte_envelope(self.envelope1, self.envelope2) or \
                self._gte_envelope(self.envelope2, self.envelope1):
            if self._compare_projection_to_height(self.envelope1,
                                                  self.envelope2) or \
               self._compare_projection_to_height(self.envelope2,
                                                  self.envelope1):
                return "You can pack one envelope in to another"
        return "You can't pack envelopes"


def continuation(prompt):
    if prompt in ["Yes", "Y", "y"]:
        return True
    return False


def inputs():
    fst_widht = input("please input width of the 1st envelope")
    fst_height = input("please input height of the 1st envelope")
    snd_widht = input("please input width of the 2st envelope")
    snd_height = input("please input height of the 2st envelope")
    return fst_widht, fst_height, snd_widht, snd_height


def run_console_interface():
    while True:
        fst_widht, fst_height, snd_widht, snd_height = inputs()
        envelope1 = Envelope(fst_widht, fst_height)
        envelope2 = Envelope(snd_widht, snd_height)
        comparator = EnvelopeComparator(envelope1, envelope2)
        print(comparator.compare_envelopes_to_pack())
        contin = input("Would you like to continue?")
        if not continuation(contin):
            break


def main():
    run_console_interface()


if __name__ == '__main__':
    main()
