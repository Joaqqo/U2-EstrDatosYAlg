from Pila import Pila

if __name__ == '__main__':
    p= Pila()
    decimal= int(input("Ingrese un número:  "))
    #binario=""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        p.Insertar(residuo)
        #binario= str(residuo) + binario
    #print("Su numero binario es: {}" .format(binario))
    print("Su número en binario es: ")
    p.Desapilar()
