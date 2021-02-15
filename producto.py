import numpy as np
def complejo(a):
    if "+" in a:
        a = a.split("+")
        a[0]=int(a[0])
        a[1]=int(a[1][:-1])
    else:
        if a[0]=="-":
            a=a.split("-")
            a[1]=int(a[1])*-1
            a[2]=int(a[2][:-1])*-1
            a=a[1::]
        else:
            a = a.split("-")
            a[0]=int(a[0])
            a[1]=int(a[1][:-1])*-1
    return a
        
def producto(a, b):

    a = complejo(a)
    b = complejo(b)
    real = a[0]*b[0] - a[1]*b[1]
    imaginario = a[0]*b[1] + a[1]*b[0]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"

