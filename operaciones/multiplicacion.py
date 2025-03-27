from operaciones.suma import sumar
from operaciones.resta import restar

def multiplicar(a, b):
    negativo = False
    if a < 0:
        a = restar(0, a)
        negativo = not negativo
    if b < 0:
        b = restar(0, b)
        negativo = not negativo

    resultado = 0
    while b > 0:
        if b & 1:
            resultado = sumar(resultado, a)
        a <<= 1
        b >>= 1

    return restar(0, resultado) if negativo else resultado
