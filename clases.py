
class Coche():
    def __init__(self):

        self.__largoChsis = 250
        self.__anchoChasis = 150
        self.__ruedas = 4
        self.__enmarcha = False

    def arranca(self, arrancamos):
        self.__enmarcha = arrancamos

        if (self.__enmarcha):
            return "el Vehiculo esta en marcha"

        else:
            return "El vehiculo esta parado"

    def estado(self):
        print("el coche tiene", self.__ruedas, "Ruedas", self.__anchoChasis, "y un largo de",
       self.__largoChsis)




carritoChiqui = Coche()


print(carritoChiqui.arranca(True))
carritoChiqui.estado()

print("--- Desupes de esta linea tenemos el segundo objeto----")

carritoChiqui2 = Coche()

print(carritoChiqui.arranca(False))
carritoChiqui.estado()

