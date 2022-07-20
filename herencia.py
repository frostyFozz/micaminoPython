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

#la clase vehiculos es la clase madre de donde se llamaran estados y sus metodos
class Camioneta(Vehiculos):
    cargar = ""
    def Carga(self, cargar):
        self.cargar = cargar
        if self.cargar:
            return "La camioneta esta Cargada!"
        else:
            return "La Camioneta esta vacia!"

# la clase camioneta tiene sus propios metodos per utiliza estados de la clase madre
class Moto(Vehiculos):
    calibra= ""
    def motoCalibrada(self):
        self.calibra = "Llevo la moto en una goma"    
    
    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nEnmarcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena, "\n", self.calibra)

#  la clase moto utiliza estados de la clase madre pero agrega un metodo propio de su clase

class VehiculoElec(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.bateria = 100
    def estadoBateria(self):
        self.Cargando = True    

# Esta es una superclase que utiliza estados de la clase madre pero agrega sus propios estados

class MotoElectric(VehiculoElec, Vehiculos):
    pass
# aqui estamos utilizando dos clases para crear una utilidad multiple en el codigo


miMoto = Moto("Harley","Runner")
miMoto.arrancar()
miMoto.motoCalibrada()
miMoto.estado()

print("--- Segundo heredero de la class vehiculos--- ")

miCamioneta = Camioneta("Ford", "F250")

miCamioneta.arrancar()
miCamioneta.estado()
print(miCamioneta.Carga(True))


print("--- estado de la motoelectrica-- ")


mielect = MotoElectric("honda", "pedal1")
mielect.estado()




