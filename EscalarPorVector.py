import componentes
import producto

def EscalarPorVector(escalar,vector):
    final = []
    for i in range(len(vector)):
        final.append(producto.producto(escalar,vector[i]))
    return final

