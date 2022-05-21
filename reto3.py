password="a,a,b,b,c,d,f,f"
caracter=password.split(",")
inicial=""
cont=0
listacontador=[]
listaletras=[]

for i in caracter:
    if inicial.upper()==i.upper():
        cont+=1
    else:
        if cont>0:
            listacontador.append(str(cont))
        inicial=i
        listaletras.append(i.upper())
        cont=1
listacontador.append(str(cont))
print(" ".join(listaletras))
print(" ".join(listacontador))

