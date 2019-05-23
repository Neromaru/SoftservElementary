import unittest

from Task2.main import EnvelopeComparator, Envelope


class TestEnvelope(unittest.TestCase):

    def test_prepare_envelope_to_pack(self):
        initial = Envelope(3, 4)
        expected = Envelope
        return self.assertIsInstance(initial.prepare_envelope_to_pack(),
                                     expected)

    def test_diagonal_calculation(self):
        initial = Envelope(3, 4)
        expected = 5
        initial.prepare_envelope_to_pack()
        return self.assertEqual(initial.diagonal, expected)

    def test_projection_calculations(self):
        initial = Envelope(3, 5)
        expected = 6.86
        initial.prepare_envelope_to_pack()
        return self.assertEqual(round(initial.projection, 2), expected)


class TestEnvelopeComparator(unittest.TestCase):

    def test_envelope_comparison(self):
        envelope1 = Envelope(3, 4)
        envelope2 = Envelope(2, 3)
        initial = EnvelopeComparator(envelope1, envelope2)
        data = {
            "You can't pack envelopes": False,
            'You can pack one envelope in to another': True
            }
        result = data.get(initial.compare_envelopes_to_pack())
        return self.assertTrue(result)

    def test_envelopes_cannot_be_packed(self):
        envelope1 = Envelope(3, 4)
        envelope2 = Envelope(3, 0.5)
        initial = EnvelopeComparator(envelope1, envelope2)
        data = {
            "You can't pack envelopes": False,
            "You can pack one envelope in to another": True
            }
        result = data.get(initial.compare_envelopes_to_pack())
        return self.assertFalse(result)
