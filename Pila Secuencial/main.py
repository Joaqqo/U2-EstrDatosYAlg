from Pila import Pila
if __name__ == '__main__':
    p=Pila()
    p.Insertar(3) #Insertar
    p.Insertar(2)
    p.Insertar(1)
    p.Insertar(4) #Pila llena
    p.Desapilar() #Desapilar
    print(p.Vacia()) #Si la pila está vacía devuelve True
