class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado_civil = Soltero(self)

    def casar(self):
        self.estado_civil.casar()
    def divorciar(self):
        self.estado_civil.divorciar()

class EstadoCivil:
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        pass
    def enviudar(self):
        pass
    def morir(self):
        pass
    def divorciar(self):
        pass

class Casado(EstadoCivil):
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        pass
    def enviudar(self):
        self.persona.estado_civil = Viudo(self.persona)
    def morir(self):
        self.persona.estado_civil = Difunto(self.persona)
    def divorciar(self):
        self.persona.estado_civil = Divorciado(self.persona)
    
    def __str__(self):
        return "Casado"

class Soltero(EstadoCivil):
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        self.persona.estado_civil = Casado(self.persona)
    def enviudar(self):
        pass
    def morir(self):
        self.persona.estado_civil = Difunto(self.persona)
    def divorciar(self):
        pass

    def __str__(self):
        return "Soltero"

class Divorciado(EstadoCivil):
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        self.persona.estado_civil = Casado(self.persona)
    def enviudar(self):
        pass
    def morir(self):
        self.persona.estado_civil = Difunto(self.persona)
    def divorciar(self):
        pass

    def __str__(self):
        return "Divorciado"

class Viudo(EstadoCivil):
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        self.persona.estado_civil = Casado(self.persona)
    def enviudar(self):
        pass
    def morir(self):
        self.persona.estado_civil = Difunto(self.persona)
    def divorciar(self):
        pass
    def __str__(self):
        return "Viudo"

class Difunto(EstadoCivil):
    def __init__(self, persona):
        self.persona = persona
    def casar(self):
        pass
    def enviudar(self):
        pass
    def morir(self):
        pass
    def divorciar(self):
        pass
    def __str__(self):
        return "Difunto"

def main():
    pepito = Persona("Pepito")
    print(pepito.estado_civil)
    pepito.casar()
    print(pepito.estado_civil)
    pepito.divorciar()
    print(pepito.estado_civil)

main()