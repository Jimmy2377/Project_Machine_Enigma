import unittest
from src.Utils.FileHandler import FileHandler
class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.input_filename = 'test_input.txt'
        self.output_filename = 'test_output.txt'
        self.content = "Test content for file handling."

    def test_read_write_file(self):
        # Escribir contenido en un archivo
        FileHandler.write_file(self.input_filename, self.content)

        # Leer el contenido del archivo y verificar si es el mismo
        read_content = FileHandler.read_file(self.input_filename)
        self.assertEqual(read_content, self.content)

        # Escribir el contenido en otro archivo
        FileHandler.write_file(self.output_filename, read_content)

        # Leer el contenido del segundo archivo y verificar si es el mismo
        read_output_content = FileHandler.read_file(self.output_filename)
        self.assertEqual(read_output_content, self.content)

        # Limpiar archivos creados durante las pruebas
        FileHandler.delete_file(self.input_filename)
        FileHandler.delete_file(self.output_filename)
if __name__ == '__main__':
    unittest.main()
