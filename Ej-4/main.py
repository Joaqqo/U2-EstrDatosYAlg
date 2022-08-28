from Pila import Pila
if __name__ == '__main__':
    p=Pila()
    p.Insertar(3, 1) #Insertar en pila A
    p.Insertar(2, 2) #Insertar en pila B
    p.Insertar(1, 2)
    p.Insertar(4, 1) #Pila llena
    print(p.Vacia(1)) #Si la pila está vacía devuelve True
    print(p.Vacia(2)) #Si la pila está vacía devuelve True
