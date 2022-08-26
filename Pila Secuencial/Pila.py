class Pila:
    __items= []
    __tope= -1
    __cant= 3

    def __init__(self, xcant=3):
        self.__items= []
        self.__tope= -1
        self.__cant= xcant


    def Vacia(self):
        return self.__tope == -1

    def Llena(self):
        return self.__tope == self.__cant-1

    def Insertar(self, x):
        if not self.Llena():
            self.__tope +=1
            self.__items.insert(self.__tope, x) #self.__items.append(x)
        else:
            print("Pila llena")

    def Suprimir(self):
        if not self.Vacia():
            x= self.__items[self.__tope] #self.__items.pop()
            self.__tope -= 1
            return x
        else:
            print("Pila vacía")

    def Desapilar(self):
        if not self.Vacia():
            for i in range(self.__tope, -1, -1): #El rango sería por ejemplo 3 2 1 0
                print(self.Suprimir())
            else:
                print("Pila vacía")


