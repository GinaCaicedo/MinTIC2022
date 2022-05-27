

lista1=["pantalón", "falda", "pantalón", "vestido", "blusa", "sudadera", "pantalón","falda","pantalón","vestido"]
inexistentes1 = [3,5,7,10,15,16]
inexistentes2 = [4,10,5,8]
codigoArticulo=[2,3,6,8]
claseArticulo="pantalón"



def grupos(lista1):
    listaUnicos = []
    for i in lista1:
        if i not in listaUnicos :
            agrega=i
            listaUnicos.append(agrega)
    return listaUnicos



def faltantes(codigoArticulo,lista1,claseArticulo):
    listaFaltantes = []

    for i in  codigoArticulo:
        if lista1[i]==claseArticulo:
            listaFaltantes.append(i)
    return listaFaltantes


def inexistentes(inexistentes1,inexistentes2):
    listaUnicosInexistentes = []
    for i in inexistentes1:
        if i not in inexistentes2:
            agrega=i
            listaUnicosInexistentes.append(agrega)
    return listaUnicosInexistentes



def trueque(inexistentes2,inexistentes1):
    listaUnicosInexistentes1 = []
    listaUnicosInexistentes = []

    for i in inexistentes2:
        if i not in inexistentes1:
            agrega1=i
            listaUnicosInexistentes1.append(agrega1)
    len(listaUnicosInexistentes1)

    for i in inexistentes1:
        if i not in inexistentes2:
            agrega=i
            listaUnicosInexistentes.append(agrega)
    len(listaUnicosInexistentes)


    if len(listaUnicosInexistentes1)>len(listaUnicosInexistentes):
        return len(listaUnicosInexistentes)

    else:
        len(listaUnicosInexistentes1) < len(listaUnicosInexistentes)
        return len(listaUnicosInexistentes1)



