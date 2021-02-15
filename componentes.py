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

def componer(a):
    if a[1]>0:
        compuesta = str(a[0])+"+"+str(a[1])+"i"
    else:
        compuesta = str(a[0])+str(a[1])+"i"

    return compuesta

