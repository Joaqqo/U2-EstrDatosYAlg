from os import system
from Pila import Pila

def Inicio(discos):
    for i in range(discos, 0, -1):
        PA.Insertar(i)
    listaP.append(PA)
    listaP.append(PB)
    listaP.append(PC)

def Fin():
    return PA.Vacia() and PB.Vacia() and PC.Llena()

def MostrarPilas():
    for i in range(len(listaP)):
        print("\nPila", i+1)
        listaP[i].Desapilar()
def Mover(origen, destino):
    destino.Insertar(origen.Suprimir())

def numPilaValido():
    origen= int(input("\n Ingrese la pila de origen:  "))
    while origen not in [1, 2, 3]:
        print("Error solo puede elegir pila 1, 2 o 3")
        origen= int(input("\n Ingrese la pila de origen:  "))

    destino= int(input("Ingrese pila de destino:  "))
    destinos=[1, 2, 3]
    destinos.remove(origen)
    while destino not in destinos:
        print("Error, pila de destino incorrecta")
        destino = int(input("Ingrese pila de destino:  "))
    return origen, destino

def movValido():
    dato=numPilaValido()
    pilaOrg=listaP[dato[0]-1]
    pilaDes=listaP[dato[1]-1]
    if not pilaOrg.Vacia():
        if not pilaDes.Llena():
            if pilaDes.Vacia() or pilaOrg.getDato() < pilaDes.getDato():
                Mover(pilaOrg, pilaDes)
                global cant
                cant += 1
            else:
                print("Error, sólo se puede apilar una pieza encima de una más grande")
                system('pause')
        else:
            print("La pila destino está llena")
    else:
        print("La pila origen está vacía")
    MostrarPilas()
    print("\n" + "-" * 29)


if __name__ == '__main__':
    print("-----Torres de Hanoi-----")
    discos= int(input("Ingrese cantidad de discos:  "))
    PA= Pila(discos) #Pila 1
    PB= Pila(discos) #Pila 2
    PC= Pila(discos) #Pila 3
    listaP= [] #Lista Pilas
    cant= 0

    Inicio(discos)
    MostrarPilas()
    while not Fin():
        movValido()
    MostrarPilas()

    print("Terminaste en", cant, "movimientos")
    print("Número mínimo de movimientos:" , 2**discos-1)
