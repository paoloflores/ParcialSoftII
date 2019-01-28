# Singleton
class Persona:
    instancia = None # De Clase

    @classmethod
    def get_instance(cls): # Metodo de clase
        if cls.instancia == None:
            cls.instancia = Persona()
        return cls.instancia

    #def __init__(self): 
    #    self.nombre = "" # De instancia

def main():
    pepito = Persona.get_instance()
    eduardo = Persona.get_instance()
    pamela = Persona.get_instance()
    
    pepito.edad = 30
    print(pamela.edad)
    eduardo.edad = 20
    print(pamela.edad)

if __name__ == "__main__":
    main()