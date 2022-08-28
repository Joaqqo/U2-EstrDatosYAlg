class Pila:
    __items= []
    __topeA= -1
    __cant= 3
    __topeB= 3

    def __init__(self, xcant=3):
        self.__items= []
        self.__topeA= -1
        self.__cant= xcant
        self.__topeB= 3

    def __str__(self):
        return f"{self.__items}"


    def Vacia(self, pila):
        vacio= None
        if pila == 1:
            vacio= self.__topeA == -1
        elif pila == 2:
            vacio= self.__topeB == self.__cant
        else:
            print("Especifique la pila por favor")
        return vacio

    def Llena(self):
        return self.__topeA+1 == self.__topeB

    def Insertar(self, x, pila):
        if not self.Llena():
            if pila == 1:
                self.__topeA +=1
                self.__items.insert(self.__topeA, x) #self.__items.append(x)
            elif pila == 2:
                self.__topeB -= 1
                self.__items.insert(self.__topeB, x)
        else:
            print("Pila llena")

    def Suprimir(self, pila):
        if not self.Vacia(pila) and pila == 1:
            x= self.__items[self.__topeA] #self.__items.pop()
            self.__topeA -= 1
            return x
        elif not self.Vacia(pila) and pila == 2:
            x= self.__items[self.__topeB]
            self.__topeB += 1
            return x
        else:
            print("Pila vacía")




