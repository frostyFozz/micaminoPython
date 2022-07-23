
import pickle
class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con el nombre", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    Personas = []

    def __init__(self):
        listaDePersonas = open("FicheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.Personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero Externo".format(len(self.Personas)))
        except:
            print("El fichero Esta vacio")

        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):
        self.Personas.append(p)

    
    def mostrarPersonas(self):
        for p  in self.Personas:
            print(p)

    def guardarPersonasenFicheroexterno(self):
        listaDePersonas = open("FicheroExterno", "wb")
        pickle.dump(self.Personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarinfoFicheroExterno(self):
        print("la informacion del fichero externo es la siguiente: ")
        for p in self.Personas:
            print(p)


   
miLista=ListaPersonas()

perona = Persona("Dannesa", "Betancourt", 30)
miLista.agregarPersonas(perona)
miLista.mostrarPersonas()
miLista.mostrarinfoFicheroExterno()
