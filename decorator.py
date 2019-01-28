
# funcion a decorar
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

# Funcion decoradora
def f_decoradora(func_a_decorar):
    def f_decorada(diccionario):
        resp = func_a_decorar(diccionario)
        return resp.upper()
    return f_decorada


def main():
    persona = {
        "nombre" : "Pepito",
        "edad" : 20
    }
    print(formatear_xml(persona)) # ejecucion de la funcion SIN decorar
    f_decorada = f_decoradora(formatear_xml)
    print(f_decorada(persona)) # ejecucion de la funcion decorada

if __name__ == "__main__":
    main()