class ConsoleView:
    def get_input(self):
        """
        Solicita al usuario que ingrese un mensaje y devuelve la entrada del usuario.

        Returns:
        - str: Mensaje ingresado por el usuario.
        """
        return input("Ingrese el mensaje: ")

    def display_output(self, output):
        """
        Muestra un mensaje en la consola.

        Args:
        - output (str): Mensaje a mostrar en la consola.
        """
        print("Resultado:", output)
