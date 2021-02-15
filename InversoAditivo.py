import numpy as np
import componentes

def InversoAditivo(vector):
    for i in range(len(vector)):
        vector[i]=componentes.componentes(vector[i])
        vector[i][0]*=-1
        vector[i][1]*=-1
        vector[i]=componentes.componer(vector[i])
    return vector

