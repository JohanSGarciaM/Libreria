import Transpuesta
import ConjugadoMatriz_Vector

def AdjuntaMatriz(matriz):
    matriz = Transpuesta.TranspuestaMatriz(matriz)
    matriz = ConjugadoMatriz_Vector.ConjugadoMatriz(matriz)
    return matriz

def AdjuntaVector(vector):
    vector = Transpuesta.TranspuestaVector(vector)
    vector = ConjugadoMatriz_Vector.ConjugadoMatriz(vector)
    return vector
