from operaciones.resta import restar
from operaciones.suma import sumar

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"

    negativo = False
    if a < 0:
        a = restar(0, a)
        negativo = not negativo
    if b < 0:
        b = restar(0, b)
        negativo = not negativo

    resultado = 0
    acumulador = 0
    for i in range(31, -1, -1):
        if (acumulador + (b << i)) <= a:
            acumulador = sumar(acumulador, b << i)
            resultado = resultado | (1 << i)

    return restar(0, resultado) if negativo else resultado
