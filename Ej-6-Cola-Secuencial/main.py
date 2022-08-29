from Cola import Cola
if __name__ == '__main__':
    Cola= Cola(3) #Máximo 3 en la cola
    Cola.Insertar(5)
    Cola.Insertar(2)
    Cola.Insertar(3)
    Cola.Insertar(4) #Cola llena
    x=Cola.Suprimir()
    print(x) #Es el 5, porque fué el primero en llegar


