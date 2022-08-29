class Pila:
    __items= []
    __tope= -1
    __cant= 3

    def __init__(self, xcant=3):
        self.__items= [0 for _ in range(xcant)]
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
            for i in range(self.__tope, -1, -1):
                blanks = i
                print(" " * (blanks + 1) + "_" * (self.__items[i] * 2 - 1) + " " * (blanks + 1))
                print(" " * blanks + "|" + " " * (self.__items[i] - 1) + str(self.__items[i])
                      + " " * (self.__items[i] - 1) + "|" + " " * blanks)
        else:
            print("Pila vacía")

    def getDato(self):
        return self.__items[self.__tope]