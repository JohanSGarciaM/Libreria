import componentes

def EscalarPorComplejo(escalar,complejo):
    componente = componentes.componentes(complejo)
    componente[0]*=escalar
    componente[1]*=escalar
    complejo = componentes.componer(componente)
    return complejo
