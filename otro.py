
cadena="r,r,r,w,w,w,p,o,r,r,q,q,q,q,q"

# def cadenaA():
#     cadena1 = cadena.upper()
#     cadena2 = cadena1.replace(",", '')
#     cadena3 = list(cadena2)
#     cadena4 =[]
#     cadena5 =[]
#
#     for i in cadena3:
#         if i not in cadena4:
#             cadena4.append(i)
#             cadena5=cadena4
#             cadena6=" ".join(cadena5)
#
#     return cadena
#
# print(cadenaA())


def cuenta():
    cadena1 = cadena.upper()
    cadena2 = cadena1.replace(",", '')
    cadena3 = list(cadena2)
    print(cadena3)
    cadena4 = []
    cadena5 = []
    cadena6 = []
    valu=1
    valus=0
    i=0
    a=0
    cont=1
    conts = 0
    b=len(cadena3)
    p=0





    while (len(cadena3)-1)>p:

        if cadena3[a] == cadena3[a+1]:
            cont+=1
            cadena4.append(cont)


        p += 1






    return cadena4,cadena5

print(cuenta())
