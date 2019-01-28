class Observado:
    def __init__(self):
        self.observadores = []
    
    def add_observer(self, observador):
        self.observadores.append(observador)

    def notificar(self):
        for obs in self.observadores:
            obs.reacciona() # <------------------------

class Observador: # Concepto generalizador
    def reacciona(self):
        pass

class Alexander(Observador):
    def reacciona(self):
        print("tomando nota en notepad") # momento 3

class Alexis(Observador):
    def reacciona(self):
        print("tomando nota en un papelito") # momento 3

def main():
    # momento 1: Inscribimos los observadores
    profesor = Observado()
    alexis = Alexis()
    alexander = Alexander()
    profesor.add_observer(alexis)
    profesor.add_observer(alexander)

    # momento 2: Generar el evento
    profesor.notificar()

if __name__ == "__main__":
    main()