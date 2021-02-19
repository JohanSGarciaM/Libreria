def componentes(a):
    if "+" in a:
        a = a.split("+")
        a[0]=int(a[0])
        a[1]=int(a[1][:-1])
    else:
        if a[0]=="-":
            a=a.split("-")
            a[1]=int(a[1])*-1
            a[2]=int(a[2][:-1])*-1
            a=a[1::]
        else:
            a = a.split("-")
            a[0]=int(a[0])
            a[1]=int(a[1][:-1])*-1
    return a


def resta (a, b):
    a = componentes(a)
    b = componentes(b)
    b[0]*=-1
    b[1]*=-1
    real = a[0]+b[0]
    imaginario = a[1]+b[1]

    return resultado(real, imaginario)

def resultado(a, b):

    if b < 0:
        b = b * -1
        return str(a) + " - " + str(b) + "i"

    return str(a) + " + " + str(b) + "i"

def main():
    print(resta("8+6i","5+2i"))
main()

