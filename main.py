from utils.menu import mostrar_menu

def main():
    print("=== Calculadora sin Operadores Aritméticos ===")
    while True:
        if not mostrar_menu():
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
