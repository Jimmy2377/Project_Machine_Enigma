import unittest
from src.Model.Rotor import Rotor
class TestRotor(unittest.TestCase):
    def test_encode_forward(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        encoded_char = rotor.encode_forward('A')
        self.assertEqual(encoded_char, 'E')

    def test_encode_backward(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        encoded_char = rotor.encode_backward('E')
        self.assertEqual(encoded_char, 'A')

    def test_rotate(self):
        rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        self.assertFalse(rotor.rotate())
        self.assertTrue(rotor.rotate())

if __name__ == '__main__':
    unittest.main()
