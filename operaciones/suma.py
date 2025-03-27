def sumar(a, b):
    MASK = 0xFFFFFFFF          # Simula 32 bits
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        carry = a & b
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK

    return a if a <= MAX_INT else ~(a ^ MASK)