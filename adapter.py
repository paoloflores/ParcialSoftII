import lib_json
from lib_xml import XMLWriter

class Persona:
    def __init__(self, nombre ,edad):
        self.nombre = nombre
        self.edad = edad

class DataAdapter:
    def escribir(self, persona):
        pass

class XMLAdapter(DataAdapter):
    def escribir(self, persona):
        writer = XMLWriter()
        writer.write(persona)

class JSONAdapter(DataAdapter):
    def escribir(self, persona):
        json = lib_json.JSON(persona)
        json.pintar()

def main():
    persona = Persona("Pepito", 30)
    adapter = JSONAdapter()
    adapter.escribir(persona)

if __name__ == "__main__":
    main()