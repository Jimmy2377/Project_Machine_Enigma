from src.Model.Rotor import Rotor
from src.Model.Reflector import Reflector
from src.Model.EnigmaMachine import EnigmaMachine
from src.Model.Plugboard import Plugboard
from src.View.ConsoleView import ConsoleView
from src.Utils.FileHandler import FileHandler

class EnigmaController:
    def __init__(self):
        """
        Inicializa el controlador con la vista y la máquina Enigma.
        """
        self.view = ConsoleView()
        self.machine = EnigmaMachine(
            self.initialize_rotors(),
            self.initialize_reflector(),
            self.initialize_plugboard()
        )

    def initialize_rotors(self):
        """
        Inicializa y retorna los rotores de la máquina Enigma.

        Returns:
        - list: Lista de rotores.
        """
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E')
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V')
        rotor4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J')
        rotor5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z')
        return [rotor1, rotor2, rotor3, rotor4, rotor5]

    def initialize_reflector(self):
        """
        Inicializa y retorna el reflector de la máquina Enigma.

        Returns:
        - Reflector: Reflector de la máquina Enigma.
        """
        return Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")

    def initialize_plugboard(self):
        """
        Inicializa y retorna el plugboard de la máquina Enigma.

        Returns:
        - Plugboard: Plugboard de la máquina Enigma.
        """
        return Plugboard({'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'})  # Ejemplo de conexiones

    def encode_message(self):
        """
        Codifica un mensaje ingresado por el usuario y lo muestra en la vista.
        """
        message = self.view.get_input()
        encoded_message = self.machine.encode(message)
        self.view.display_output(encoded_message)

    def decode_message(self):
        """
        Decodifica un mensaje ingresado por el usuario y lo muestra en la vista.
        """
        message = self.view.get_input()
        decoded_message = self.machine.decode(message)
        self.view.display_output(decoded_message)

    def encode_file(self, input_file, output_file):
        """
        Lee un archivo de entrada, codifica su contenido y escribe el resultado en un archivo de salida.

        Args:
        - input_file (str): Nombre del archivo de entrada.
        - output_file (str): Nombre del archivo de salida.
        """
        content = FileHandler.read_file(input_file)
        encoded_content = self.machine.encode(content)
        FileHandler.write_file(output_file, encoded_content)

    def decode_file(self, input_file, output_file):
        """
        Lee un archivo de entrada, decodifica su contenido y escribe el resultado en un archivo de salida.

        Args:
        - input_file (str): Nombre del archivo de entrada.
        - output_file (str): Nombre del archivo de salida.
        """
        content = FileHandler.read_file(input_file)
        decoded_content = self.machine.decode(content)
        FileHandler.write_file(output_file, decoded_content)
