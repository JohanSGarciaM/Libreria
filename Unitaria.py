import Adjunta
import ProductoMatrices
import EscalarPorMatriz

def unitaria(matriz):
    adjunta = Adjunta.AdjuntaMatriz(matriz)
    resultado = ProductoMatrices.ProductoMatrices(matriz,adjunta)
    unitaria = True
    for i in range(len(resultado)):
        if resultado[i][i]!= "1+0i":
            unitaria = False 
    return unitaria

    
    
