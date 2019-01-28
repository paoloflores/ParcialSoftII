# Funcion decoradora
def convertir_mayusculas(func_a_decorar):
    def f_decorada(diccionario):
        resp = func_a_decorar(diccionario)
        return resp.upper()
    return f_decorada

# funcion a decorar
@convertir_mayusculas
def formatear_xml(diccionario):
    '''
    diccionario = {
        "nombre" : "Pepito",
        "edad" : 20
     }
    '''
    cad = "<data>\n"
    for llave, valor in diccionario.items():
        cad += "\t<{}>{}</{}>\n".format(llave, valor, llave)
    cad += "</data>"
    return cad

def main():
    persona = {
        "nombre" : "Pepito",
        "edad" : 20
    }
    print(formatear_xml(persona))

if __name__ == "__main__":
    main()