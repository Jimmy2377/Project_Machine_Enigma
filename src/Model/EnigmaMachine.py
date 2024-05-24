from src.Model.Plugboard import Plugboard
class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard=None):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard if plugboard else Plugboard()
        self.initial_positions = [rotor.position for rotor in rotors]

    def reset_rotors(self):
        for rotor, position in zip(self.rotors, self.initial_positions):
            rotor.position = position

    def encode(self, message):
        encoded_message = ""
        for char in message:
            if char.isalpha():
                char = char.upper()
                char = self.plugboard.connect(char)
                char = self.pass_through_rotors(char, forward=True)
                char = self.reflector.reflect(char)
                char = self.pass_through_rotors(char, forward=False)
                char = self.plugboard.connect(char)
                self.rotate_rotors()
            encoded_message += char
        return encoded_message

    def decode(self, message):
        self.reset_rotors()
        return self.encode(message)

    def pass_through_rotors(self, char, forward=True):
        for rotor in self.rotors if forward else reversed(self.rotors):
            if forward:
                char = rotor.encode_forward(char)
            else:
                char = rotor.encode_backward(char)
        return char

    def rotate_rotors(self):
        for rotor in self.rotors:
            if not rotor.rotate():
                break