import unittest
from src.Model.EnigmaMachine import EnigmaMachine
from src.Model.Rotor import Rotor
from src.Model.Reflector import Reflector

class TestEnigmaMachine(unittest.TestCase):
    def setUp(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E')
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
        reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.machine = EnigmaMachine([rotor1, rotor2, rotor3], reflector)

    def test_encode_decode(self):
        message = "HELLO"
        encoded_message = self.machine.encode(message)
        decoded_message = self.machine.decode(encoded_message)
        self.assertEqual(decoded_message, message)
if __name__ == '__main__':
    unittest.main()
