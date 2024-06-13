import unittest
from src.Model.Rotor import Rotor


class TestRotor(unittest.TestCase):
    def test_encode_forward(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        encoded_char = rotor.encode_forward('Q')
        self.assertEqual(encoded_char, 'X')

    def test_encode_backward(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        encoded_char = rotor.encode_backward('I')
        self.assertEqual(encoded_char, 'V')

if __name__ == "__main__":
    unittest.main()
