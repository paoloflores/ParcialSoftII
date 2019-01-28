class JSON:
    def __init__(self, persona):
        self.persona = persona
    def pintar(self):
        print("{{ 'nombre': {} , 'edad' : {} }} ".format(
            self.persona.nombre, self.persona.edad))