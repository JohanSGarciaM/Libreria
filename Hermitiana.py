import Adjunta

def Hermitiana(matriz):
    adjunta = Adjunta.AdjuntaMatriz(matriz)
    hermi = True
    if len(matriz)==len(adjunta) and len(matriz[0])==len(adjunta[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j]!=adjunta[i][j]:
                    hermi=False
    else:
        hermi =False
    return hermi
