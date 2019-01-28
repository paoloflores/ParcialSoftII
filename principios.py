class Persona:
    def __init__(self, mascota, nombre):
        self.mascota = mascota
        self.nombre = nombre

    def llegar_a_casa(self):
        self.mascota.acariciar() # Aca sucede el mensaje: Persona ---> Perro

    def dar_comer(self):
        print("{} da de comer a {} ".format(self.nombre, self.mascota.nombre))


class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.duenho = None

    def set_duenho(self, persona):
        self.duenho = persona

    def hambre(self):
        pass
    
    def acariciar(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
    
    def hambre(self):
        self.duenho.dar_comer()  # Perro ----> Persona

    def acariciar(self):
        print("El perrito {} mueve la cola".format(self.nombre))

class Gato(Mascota):
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
    
    def hambre(self):
        print("Ronronea")
        self.duenho.dar_comer()  # Perro ----> Persona

    def acariciar(self):
        print("El gato {} se va.".format(self.nombre))

def main():
    #sila = Perro("Sila")
    michi = Gato("michi")
    pepito = Persona(michi, "Pepito")

    pepito.llegar_a_casa() #   Funcion (main) -------> Persona

main()