#Reto1

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

