class ComponenteRestaurante:
    def calcular_ventas(self):
        pass

class CadenaRestomiel(ComponenteRestaurante):
    def __init__(self):
        self.hijos = []
    def calcular_ventas(self):
        ventas_total = 0
        for elem in self.hijos:
            ventas_total += elem.calcular_ventas()
        return  ventas_total
    def add_hijo(self, componente):
        self.hijos.append(componente)

class ComidaMarina(ComponenteRestaurante):
    def __init__(self):
        self.hijos = []
    def calcular_ventas(self):
        ventas_total = 0
        for elem in self.hijos:
            ventas_total += elem.calcular_ventas()
        return  ventas_total

    def add_hijo(self, componente):
        self.hijos.append(componente)

class ComidaCriolla(ComponenteRestaurante):
    def __init__(self):
        self.hijos = []
    def calcular_ventas(self):
        ventas_total = 0
        for elem in self.hijos:
            ventas_total += elem.calcular_ventas()
        return  ventas_total

    def add_hijo(self, componente):
        self.hijos.append(componente)

class ComidaInternacional(ComponenteRestaurante):
    def __init__(self):
        self.hijos = []
    def calcular_ventas(self):
        ventas_total = 0
        for elem in self.hijos:
            ventas_total += elem.calcular_ventas()
        return  ventas_total

    def add_hijo(self, componente):
        self.hijos.append(componente)

class Ceviche(ComponenteRestaurante):
    def calcular_ventas(self):
        return 200

class CausaRellena(ComponenteRestaurante):
    def calcular_ventas(self):
        return 120

class Makis(ComponenteRestaurante):
    def calcular_ventas(self):
        return 220

def main():
    # Armar la estructura
    cr = CadenaRestomiel()
    cm = ComidaMarina()
    cc = ComidaCriolla()
    ci = ComidaInternacional()
    ceviche = Ceviche()
    causa_rellena = CausaRellena()
    makis = Makis()

    ci.add_hijo(makis)
    cc.add_hijo(causa_rellena)
    cm.add_hijo(ceviche)

    cr.add_hijo(cm)
    cr.add_hijo(ci)
    cr.add_hijo(cc)

    ventas = cr.calcular_ventas()
    print("La cadena restomiel vendio {}".format(ventas))
    ventas_internacional = ci.calcular_ventas()
    print("Los platos de comida internacional vendieron {}".format(ventas_internacional))

if __name__ == "__main__":
    main()