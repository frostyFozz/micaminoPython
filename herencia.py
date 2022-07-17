class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelera(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha,
         "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)
     
class Camioneta(Vehiculos):
    cargar = ""
    def Carga(self, cargar):
        self.cargar = cargar
        if self.cargar:
            return "La camioneta esta Cargada!"
        else:
            return "La Camioneta esta vacia!"

class Moto(Vehiculos):
    calibra= ""
    def motoCalibrada(self):
        self.calibra = "Llevo la moto en una goma"    
    
    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena, "\n", self.calibra)

class VehiculoElec():
    def __init__(self):
        self.bateria = 100
    def estadoBateria(self):
        self.Cargando = True    
    

miMoto = Moto("Harley","Runner")
miMoto.arrancar()
miMoto.motoCalibrada()
miMoto.estado()

print("--- Segundo heredero de la class vehiculos--- ")

miCamioneta = Camioneta("Ford", "F250")

miCamioneta.arrancar()
miCamioneta.estado()
print(miCamioneta.Carga(True))





