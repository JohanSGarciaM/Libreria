import producto
import Suma

def ProductoInterno(vector1,vector2):
    res = "0+0i"
    for i in range(len(vector1)):
        res = Suma.suma(res,producto.producto(vector1[i],vector2[i]))
    return res
