from Cola import Cola
if __name__ == '__main__':
    Cola=Cola()
    print(Cola.Vacia()) #Devuelve True si está vacía
    Cola.Insertar(3)
    Cola.Insertar(2)
    Cola.Insertar(4)
    print(Cola.Vacia()) #Devuelve Flase porque no está vacía
    print(Cola.Suprimir()) #Devuelve el primero de la cola que sería 3
