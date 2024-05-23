from src.Controller.EnigmaController import EnigmaController

def main():
    controller = EnigmaController()
    while True:
        print("1. Codificar mensaje")
        print("2. Decodificar mensaje")
        print("3. Codificar archivo")
        print("4. Decodificar archivo")
        print("5. Salir")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            controller.encode_message()
        elif choice == '2':
            controller.decode_message()
        elif choice == '3':
            input_file = input("Ingrese el nombre del archivo de entrada: ")
            output_file = input("Ingrese el nombre del archivo de salida: ")
            controller.encode_file(input_file, output_file)
        elif choice == '4':
            input_file = input("Ingrese el nombre del archivo de entrada: ")
            output_file = input("Ingrese el nombre del archivo de salida: ")
            controller.decode_file(input_file, output_file)
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

