# Reto1
"""
Los años que lleva de fundada la población de  “Pueblo Nuevo”, menos 4 es igual a el doble de los años que lleva fundada la población
“Caserío Feliz”. Además, la suma de los años que llevan fundadas ambas poblaciones es igual a 5 veces la cantidad de años que lleva
fundada la población de “Anserma”.
Dada la cantidad de años que lleva fundada la población “Caserío Feliz, calcule la cantidad de años que llevan fundadas cada una de las
poblaciones “Pueblo Nuevo” y “La Esperanza”.
También se requiere clasificar la población “La Esperanza” dependiendo de la cantidad de años que lleva de fundada, así:
· Si esta entre 0 y 20 años se clasifica como categoría uno
· Si esta entre 21 y 40 se clasifica como categoría dos.
· Si esta entre 41 y 80 se clasifica como categoría tres.
· Si es mayor que 80 se clasificada como categoría cuatro.

"""
caserioFeliz = int(input())
puebloNuevo = int(2 * caserioFeliz + 4)
Anserma = int((puebloNuevo + caserioFeliz) / 5)
print(caserioFeliz, puebloNuevo, Anserma)


def clasificar():
    if (0 <= Anserma <= 20):
        print("uno")
    elif (21 <= Anserma <= 40):
        print("dos")
    elif (41 <= Anserma <= 79):
        print("tres")
    elif (Anserma >= 80):
        print("cuatro")


clasificar()
