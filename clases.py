
class Coche():
    def __init__(self):

        self.__largoChsis = 250
        self.__anchoChasis = 150
        self.__ruedas = 4
        self.__enmarcha = False

    def arranca(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            check = self.__check_intern()
            
        if self.__enmarcha and check:
            return "el Vehiculo esta en marcha"
          
        elif self.__enmarcha and check==False:
            return "Algo anda mal con el vehiculo por lo cual no podemos arrancar!"

        else:
            return "El vehiculo esta parado"

    def estado(self):
        print("el coche tiene", self.__ruedas, "Ruedas", self.__anchoChasis, "y un largo de",
       self.__largoChsis)

    def __check_intern(self):
        print("el checeo interno del vehiculo esta en orden")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "ok"
        self.frenoDemano = "ok"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "ok" and self.frenoDemano == "ok":
            return True
        else:
            return False



carritoChiqui = Coche()


print(carritoChiqui.arranca(True))
carritoChiqui.estado()

print("--- Desupes de esta linea tenemos el segundo objeto----")


print(carritoChiqui.arranca(False))
carritoChiqui.estado()

