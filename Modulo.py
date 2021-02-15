import componentes
def modulo(a):
    a = componentes.componentes(a)
    a[0] = a[0]**2
    a[1] = a[1]**2
    respuesta = a[0]+a[1]
    respuesta = respuesta**(1/2)
    return round(respuesta,2)
