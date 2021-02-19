import Conjugado

def ConjugadoVector(vector):
    for i in range(len(vector)):
        vector[i] = Conjugado.conjugado(vector[i])
    return vector

def ConjugadoMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = ConjugadoVector(matriz[i])

    return matriz


