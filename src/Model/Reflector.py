class Reflector:
    def __init__(self, wiring):
        """
        Inicializa el reflector con su configuración de cableado.

        Args:
        - wiring (str): Configuración de cableado del reflector.
        """
        self.wiring = wiring

    def reflect(self, char):
        """
        Refleja un carácter pasándolo a través del reflector.

        Args:
        - char (str): Carácter a reflejar.

        Returns:
        - str: Carácter reflejado.
        """
        return self.wiring[ord(char) - ord('A')]
