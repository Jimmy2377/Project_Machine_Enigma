import unittest
from src.Model.Plugboard import Plugboard

class TestPlugboard(unittest.TestCase):
    def test_connect(self):
        plugboard = Plugboard({'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'})
        connected_a = plugboard.connect('A')
        connected_b = plugboard.connect('B')
        connected_c = plugboard.connect('C')
        connected_d = plugboard.connect('D')
        self.assertEqual(connected_a, 'B')
        self.assertEqual(connected_b, 'A')
        self.assertEqual(connected_c, 'D')
        self.assertEqual(connected_d, 'C')

if __name__ == '__main__':
    unittest.main()
