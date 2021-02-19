import componentes

def conjugado(complexnum):
    complejo = componentes.componentes(complexnum)
    complejo[1]*=-1
    return componentes.componer(complejo)

