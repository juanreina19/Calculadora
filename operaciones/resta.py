from operaciones.suma import sumar

def restar(a, b):
    return sumar(a, sumar(~b, 1))
