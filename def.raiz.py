from logging.config import valid_ident
import math

def calcularRaiz(num1):

    if num1 < 0 :
        raise ValueError("No se puede encontrar la raiz de 0!")

    else:
        return math.sqrt(num1)



numUno = int(input("Introdusca el numero para la raiz: "))

try:

    print(calcularRaiz(numUno))

except ValueError as errorNumeroNegativo:
    print(errorNumeroNegativo)


print("probando que aun el programa funciona")
