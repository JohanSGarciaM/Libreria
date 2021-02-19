import componentes
import EscalarPorVector

def EscalarPorMatriz(escalar,matriz):
    for i in range(len(matriz)):
        matriz[i] = EscalarPorVector.EscalarPorVector(escalar,matriz[i])
    return matriz


        
