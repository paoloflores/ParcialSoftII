class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado_civil = 'S'

    def casar(self):
        if self.estado_civil == 'S' or self.estado_civil == 'V' or self.estado_civil == 'D':
            self.estado_civil = 'C'
    
    def divorciar(self):
        if self.estado_civil == 'C':
            self.estado_civil = 'D'
    
    def morir(self):
        self.estado_civil = 'M'
    
    def enviudar(self):
        if self.estado_civil == 'C':
            self.estado_civil = 'V'
    
def main():
    pepito = Persona("Pepito")
    print(pepito.estado_civil)
    pepito.divorciar()
    print(pepito.estado_civil)

main()