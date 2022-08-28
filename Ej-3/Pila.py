from Nodo import Nodo
class Pila:
    __tope= None

    def __init__(self):
        self.__tope= None

    def Vacia(self):
        return self.__tope is None

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

    def Desapilar(self, num):
        if self.Vacia():
            print("Pila vacía")
        else:
            result=self.__tope.getDato()
            aux= self.__tope
            while aux is not None:
                result *= self.Suprimir().getDato()
                #print(self.Suprimir().getDato())
                aux= aux.getSiguiente()
            print("El factorial de {} es {}" .format(num, result))


    def Factorial(self, num):
        if num<0:
            print("El número ingresado es negativo")
        elif num == 0:
            print("El factorial de 0 es 1")
        else:
            for i in range(num, 0, -1): #Si el número es 3, los números se muestran de la forma 3 - 2 - 1
                self.Insertar(i)
            self.Desapilar(num)
