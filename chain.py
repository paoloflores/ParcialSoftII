class EmpleadoRestaurante:
    def __init__(self):
        self.sucesor = None
    def resolver_reclamo(self, reclamo):
        pass
    def add_sucesor(self, sucesor):
        self.sucesor = sucesor

class Mozo(EmpleadoRestaurante):
    def __init__(self):
        EmpleadoRestaurante.__init__(self)
    def resolver_reclamo(self, reclamo):
        if reclamo.monto > 10:
            # Mozo no lo puede resolver
            self.sucesor.resolver_reclamo(reclamo)
        else:
            print("El mozo resolvio el reclamo")

class JefeMozos(EmpleadoRestaurante):
    def __init__(self):
        EmpleadoRestaurante.__init__(self)
    def resolver_reclamo(self, reclamo):
        if reclamo.monto > 50:
            # No lo puede resolver el Jefe
            self.sucesor.resolver_reclamo(reclamo)
        else:
            print("El Jefe de Mozos resuelve el reclamo")

class Administrador(EmpleadoRestaurante):
    def __init__(self):
        EmpleadoRestaurante.__init__(self)
    def resolver_reclamo(self, reclamo):
        if reclamo.monto > 100:
            # No lo puede resolver el Jefe
            self.sucesor.resolver_reclamo(reclamo)
        else:
            print("El Administrador resuelve el reclamo")

class AreaLegal(EmpleadoRestaurante):
    def __init__(self):
        EmpleadoRestaurante.__init__(self)
    def resolver_reclamo(self, reclamo):
        print("El Area Legal resuelve el reclamo")

class Reclamo:
    def __init__(self, monto):
        self.monto = monto

def main():
    # Armar la estructura de decision
    mozo = Mozo()
    jefe = JefeMozos()
    admin = Administrador()
    area_legal = AreaLegal()

    mozo.add_sucesor(jefe)
    jefe.add_sucesor(admin)
    admin.add_sucesor(area_legal)

    reclamo = Reclamo(34)

    mozo.resolver_reclamo(reclamo)


main()