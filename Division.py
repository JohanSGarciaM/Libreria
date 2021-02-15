import Conjugado
import componentes
import producto






def division(a, b):
    b1 = Conjugado.conjugado(b)
    axb1 = producto.producto(a,b1)
    bxb1 = producto.producto(b,b1)
    axb1 = componentes.componentes(axb1)
    bxb1 = componentes.componentes(bxb1)[0]
    real = axb1[0]/bxb1
    imaginario = axb1[1]/bxb1
    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(round(a,2)) + " - " + str(round(b,2)) + "i"

    return str(round(a,2)) + " + " + str(round(b,2)) + "i"

