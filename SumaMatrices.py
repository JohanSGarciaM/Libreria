import componentes
import Suma


def SumaMatrices(matriz1,matriz2):
    final=[]
    for i in range(len(matriz1)):
        row=[]
        for j in range(len(matriz1[i])):
            row.append(Suma.suma(matriz1[i][j],matriz2[i][j]))
        final.append(row)
    return final
