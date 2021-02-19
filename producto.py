import numpy as np
import componentes

def producto(a, b):

    a = componentes.componentes(a)
    b = componentes.componentes(b)
    real = a[0]*b[0] - a[1]*b[1]
    imaginario = a[0]*b[1] + a[1]*b[0]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + "-" + str(b) + "i"

    return str(a) + "+" + str(b) + "i"


