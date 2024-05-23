from src.Model.Plugboard import Plugboard

class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard=None):
        """
        Inicializa la máquina Enigma con los componentes necesarios.

        Args:
        - rotors (list): Lista de rotores.
        - reflector (Reflector): Reflector de la máquina.
        - plugboard (Plugboard, optional): Plugboard de la máquina, si se proporciona.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard if plugboard else Plugboard()

    def encode(self, message):
        """
        Codifica un mensaje utilizando la configuración actual de la máquina.

        Args:
        - message (str): Mensaje a codificar.

        Returns:
        - str: Mensaje codificado.
        """
        encoded_message = ""
        for char in message:
            char = self.plugboard.connect(char)
            char = self.pass_through_rotors(char, forward=True)
            char = self.reflector.reflect(char)
            char = self.pass_through_rotors(char, forward=False)
            char = self.plugboard.connect(char)
            self.rotate_rotors()
            encoded_message += char
        return encoded_message

    def decode(self, message):
        """
        Decodifica un mensaje utilizando la configuración actual de la máquina.

        Args:
        - message (str): Mensaje a decodificar.

        Returns:
        - str: Mensaje decodificado.
        """
        return self.encode(message)  # La decodificación en Enigma es simétrica a la codificación

    def pass_through_rotors(self, char, forward=True):
        """
        Pasa un carácter a través de los rotores en la dirección especificada.

        Args:
        - char (str): Carácter a pasar a través de los rotores.
        - forward (bool, optional): Dirección de paso a través de los rotores. True para hacia adelante, False para hacia atrás.

        Returns:
        - str: Carácter después de pasar a través de los rotores.
        """
        for rotor in self.rotors if forward else reversed(self.rotors):
            if forward:
                char = rotor.encode_forward(char)
            else:
                char = rotor.encode_backward(char)
        return char

    def rotate_rotors(self):
        """
        Rota los rotores y verifica si se debe avanzar el siguiente rotor.
        """
        for rotor in self.rotors:
            if not rotor.rotate():
                break
