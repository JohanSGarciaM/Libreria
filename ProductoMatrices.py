import Suma
import producto

def ProductoMatrices(matrizA,matrizB):
    if len(matrizA[0]) != len(matrizB):
        return (-1)
    else:
        matrizProducto = [["" for j in range(len(matrizA[0]))]for i in range(len(matrizA))]
        for i in range(len(matrizA)):
            for j in range(len(matrizA[0])):
                res="0+0i"
                for k in range(len(matrizA[0])):
                    multi = producto.producto(matrizA[i][k],matrizB[k][j])
                    res = Suma.suma(res,str(multi))
                matrizProducto[i][j]=res
        return matrizProducto

                
