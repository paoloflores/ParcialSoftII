class XMLWriter:
    def write(self, persona):
        print("<persona nombre={} edad={} />".format(
            persona.nombre, persona.edad))