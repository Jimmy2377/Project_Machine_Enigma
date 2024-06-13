import os
class FileHandler:
    @staticmethod
    def read_file(filename):
        """
        Lee el contenido de un archivo y lo devuelve como una cadena de texto.
        """
        with open(filename, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def write_file(filename, content):
        """
        Escribe contenido en un archivo.
        """
        with open(filename, 'w') as file:
            file.write(content)

    @staticmethod
    def delete_file(filename):
        """
        Elimina un archivo del sistema.
        """
        if os.path.exists(filename):
            os.remove(filename)
