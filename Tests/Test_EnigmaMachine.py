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

    def reset_rotors(self):
        """
        Resetea los rotores a su posición inicial para asegurar que la decodificación sea correcta.
        """
        self.machine.rotors[0].position = 0
        self.machine.rotors[1].position = 0
        self.machine.rotors[2].position = 0

    def test_encode_decode(self):
        message = "HELLO"
        encoded_message = self.machine.encode(message)
        self.reset_rotors()  # Reseteamos los rotores antes de la decodificación
        decoded_message = self.machine.decode(encoded_message)
        self.assertEqual(decoded_message, message)

    def test_encode_decode_with_spaces_and_lowercase(self):
        message = "Hello world"
        encoded_message = self.machine.encode(message)
        self.reset_rotors()  # Reseteamos los rotores antes de la decodificación
        decoded_message = self.machine.decode(encoded_message)
        self.assertEqual(decoded_message, message.upper())

if __name__ == "__main__":
    unittest.main()
