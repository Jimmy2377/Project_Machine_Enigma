class Plugboard:
    def __init__(self, connections=None):
        """
        Inicializa el plugboard con las conexiones proporcionadas.

        Args:
        - connections (dict, optional): Diccionario que mapea un carácter a otro.
                                         Por ejemplo, {'A': 'B', 'C': 'D'} indica que A se conecta a B y C se conecta a D.
        """
        self.connections = connections if connections else {}

    def connect(self, char):
        """
        Conecta un carácter a través del plugboard.

        Args:
        - char (str): Carácter a conectar.

        Returns:
        - str: Carácter conectado.
        """
        return self.connections.get(char, char)
