import InversoAditivo

def InversaAditivaMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i]=InversoAditivo.InversoAditivo(matriz[i])
    return matriz

        
