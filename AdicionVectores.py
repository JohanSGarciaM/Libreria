import numpy
import Suma

def adicionVectores(a,b):
    final=[]
    for i in range(len(a)):
        final.append(Suma.suma(a[i],b[i]))
    return final
     
