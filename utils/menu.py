from operaciones import suma, resta, multiplicacion, division

def mostrar_menu():
    print("\nSeleccione la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Opción: ").strip()

    if opcion == '5':
        return False

    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada inválida.")
        return True

    if opcion == '1':
        resultado = suma.sumar(a, b)
    elif opcion == '2':
        resultado = resta.restar(a, b)
    elif opcion == '3':
        resultado = multiplicacion.multiplicar(a, b)
    elif opcion == '4':
        resultado = division.dividir(a, b)
    else:
        print("Opción inválida.")
        return True

    print(f"El resultado es: {resultado}")
    return True
