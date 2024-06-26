class Rotor:
    def __init__(self, wiring, notch):
        """
        Inicializa un rotor con su configuración de cableado y posición de muesca.
        - wiring : Configuración de cableado del rotor.
        - notch : Letra en la que el rotor debe avanzar el siguiente rotor.
        """
        self.wiring = wiring
        self.notch = notch
        self.position = 0

    def encode_forward(self, char):  # Carácter a codificar
        """
        Codifica un carácter pasándolo a través del rotor en la dirección hacia adelante.

        """
        index = (ord(char) - ord('A') + self.position) % 26
        return self.wiring[index]   # Carácter codificado

    def encode_backward(self, char):
        """
        Codifica un carácter pasándolo a través del rotor en la dirección hacia atrás.
        """
        index = (self.wiring.index(char) - self.position) % 26
        return chr(index + ord('A'))

    def rotate(self):
        """
        Rota el rotor y verifica si debe avanzar el siguiente rotor.

        Returns:
        - bool: True si el siguiente rotor debe avanzar, False en caso contrario.
        """
        self.position = (self.position + 1) % 26
        return self.position == (ord(self.notch) - ord('A') + 1) % 26 or self.position == (ord(self.notch) - ord('A')) % 26