from Nodo import Nodo
class Pila:
    __tope= None


    def __init__(self):
        self.__tope= None


    def Vacia(self):
        return self.__tope is None

    def mostrar(self):
        print(self.__tope)

    def Insertar(self, dato):
        nodo= Nodo(dato)
        nodo.setSiguiente(self.__tope)
        self.__tope= nodo

    def Suprimir(self):
        if self.Vacia():
            print("Pila vacía")
        else:
            aux= self.__tope
            self.__tope= aux.getSiguiente()
            return aux

    def Desapilar(self):
        if self.Vacia():
            print("Pila vacía")
        else:
            aux= self.__tope
            while aux is not None:
                print(self.Suprimir().getDato())
                aux= aux.getSiguiente()
