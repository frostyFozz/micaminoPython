
class Coche():
    def desplazamiento(self):
        print("me desplazo en 4 Ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo en 2 Rueda")

class Camion():
    def desplazamiento(self):
        print("Me desplazo en 8 Ruedas")


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = Coche()
desplazamientoVehiculo(miVehiculo)

miveHiculo = Moto()
desplazamientoVehiculo(miveHiculo)

mivehiCulo = Camion()
desplazamientoVehiculo(mivehiCulo)