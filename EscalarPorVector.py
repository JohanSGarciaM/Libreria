import componentes
import EscalarPorComplejo

def EscalarPorVector(escalar,vector):
    final = []
    for i in range(len(vector)):
        final.append(EscalarPorComplejo.EscalarPorComplejo(escalar,vector[i]))
    return final

