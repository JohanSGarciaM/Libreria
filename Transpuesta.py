def TranspuestaMatriz(matriz):
    rows=[]
    for i in range(len(matriz[0])):
        column=[]
        for j in range(len(matriz)):
            column+=[matriz[j][i]]
        rows.append(column)
    return rows


def TranspuestaVector(vector):

    NuevoVector = []
    for i in range(len(vector)):
        NuevoVector.append([vector[i]])
    return NuevoVector
