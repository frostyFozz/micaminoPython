class Persona():
    def __init__(self, nombre, edad, lugar_dondevive):
        self.nombre = nombre
        self.edad = edad
        self.lugar_dondevive = lugar_dondevive
    def descripcion(self):
        print("nombre: ", self.nombre, "Edad: ", self.edad, "vivienda: ", self.lugar_dondevive)


class Empleado(Persona):
    def __init__(self, salario, vigencia, nombre_emplado, edad_empleado, lugar_empleado):
        super().__init__(nombre_emplado, edad_empleado, lugar_empleado)
        self.salario = salario
        self.vigencia = vigencia
    def descripcion(self):
        super().descripcion()
        print("salario:", self.salario, "Vigencia: ", self.vigencia)


class Contratista(Persona):
    def __init__(self, nombre, edad, lugar_dondevive, contrato):
        super().__init__(nombre, edad, lugar_dondevive)
        self.contrato = contrato
    def descripcion(self):
        super().descripcion()
        print("tiempo de contrato", self.contrato)

manuel=Empleado(31500,5,"manuel", 28, "manoguayabo")
manuel.descripcion()
print(isinstance(manuel, Empleado))

print("---Tabla de un contratista de la empresa---")

jorge = Contratista("jorge", 35, "Villa Mella", 2)
jorge.descripcion()
print(isinstance(jorge, Contratista))
        

