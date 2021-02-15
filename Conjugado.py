def complejo(a):
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

def conjugado(complexnum):
    componentes = complejo(complexnum)
    componentes[1]*=-1
    return resultado(componentes)

def resultado(numero):
    if numero[1]>0:
        return str(numero[0])+"+"+str(numero[1])+"i"
    else:
        return str(numero[0])+str(numero[1])+"i"
