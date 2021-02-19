import componentes

def suma(a , b):
    a = componentes.componentes(a)
    b = componentes.componentes(b)
    real = a[0] + b[0]
    imaginario = a[1] + b[1]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + "-" + str(b) + "i"

    return str(a) + "+" + str(b) + "i"

