"""Uso de while con contador"""

# numerosImpares=0
# numerosPares=0
#
# numero=int(input("Ingrese un numero:"))
#
# while numero !=0:
#     #verifica impar
#     if numero %2==1:
#         #contador de impares
#         numerosImpares+=1
#
#     else:
#         # contador de pares
#         numerosPares += 1
#
#     numero=int(input("Introduce numero o escriba 0 para detener"))
#
# print("Numero impares",numerosImpares)
# print("Numeros pares",numerosPares)

"""Break"""

# print("La instruccion de ruptura:")
#
# for i in range(1,6):
#     if i ==3:
#         break
#     print("Dentro del ciclo.")
# print("Fuera del ciclo.")


"""Continue"""

# print("\n La instruccion continue:")
#
# for i in range(1,6):
#
#     if i==3:
#         continue
#     print("Dentro del ciclo.",i)
#
# print("Fuera del ciclo")

"""Cupacabra -break"""

# palabraSecreta="Chupacabra"
# palabra= input("Ingrese la palabra secreta:")
#
# while True:
#     if palabra==palabraSecreta:
#         break
#     else:
#         palabra = input("Ingrese la palabra secreta:")
# print("HAS DEJADO EL CICLO CON EXITO")




# Come palabras

# userWord = str(input("Ingrese una palabra"))
#
# for letra in userWord:
#     # Completa el cuerpo del ciclo for.}
#     if  letra =="a" or letra=="e" or letra =="i" or letra=="o" or letra =="u":
#         continue
#     else:
#         print(letra)



###

# for i in range(1,1000,2):
#
#     print (i)
#



def Moderador():
    s_return=""
    s = ""
    cv = 0
    cf =0
    for m in (moderador):
        s=m

        for v in (valentina):
            if v==s:
                cv +=1

        for f in (felipe):
            if f==s:
                cf +=1

        if cv==cf:
            s_return+="≈"
            #print("≈", end="")
        elif cf>cv:
            s_return += "F"
            #print("F",end="")
        elif cf<cv:
            s_return += "V"
            #print("V",end="")

    return s_return

valentina=str(input(""))
felipe=str(input(""))
moderador=str(input(""))
print(str(Moderador()))


# def min_maquina():
#     Xi = 1.0
#     bandera = True
#
#     while(bandera or Xi > 0.0):
#         bandera = False
#
#         Xo = Xi
#         Xi = Xo / 2.0
#
#     return Xo
# print("El m ́ınimo n ́umero positivo", end = " ")
# print("en esta m ́aquina es:", min_maquina())




