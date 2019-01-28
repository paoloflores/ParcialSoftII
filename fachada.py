from adapter import JSONAdapter, XMLAdapter,Persona
import sys

class AdapterFactory:
    def obtener_adapter(self, tipo):
        if tipo == "xml":
            return XMLAdapter()
        elif tipo == "json":
            return JSONAdapter()
        else:
            return None

#Fachada
class PersonasManager:
    def imprimir_persona(self, persona, formato):
        factory = AdapterFactory()
        adapter = factory.obtener_adapter(formato)
        adapter.escribir(persona)

def main():
    manager = PersonasManager()
    manager.imprimir_persona(Persona("Pepe", 30), sys.argv[1])

if __name__ == "__main__":
    main()