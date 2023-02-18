import xml.etree.cElementTree as ET 
from xml.dom import minidom
from acceso import *
from Plataformas import ListaPlataforma

## LEEER Y EXTRACCION DE DATOS DEL XML
try:
    # print("Infrese la direccion del documento: ")
    # entrada = input()
    doc = minidom.parse("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/Practica1/salida.xml")

    print("Ya paso")


    mi_plataforma = ListaPlataforma() 
    print("-----------Acceso específico-----------")
    JuegosViejos = doc.getElementsByTagName("JuegosViejos")
    print("Tamaño JuegosViejos: ", len(JuegosViejos))
    for JuegoViejo in JuegosViejos:
        ListaPlataformas = JuegoViejo.getElementsByTagName("ListaPlataformas")
        print("Tamaño ListaPlatformas:", len(ListaPlataformas))
        for UnaPlataforma in ListaPlataformas:
            Plataformas = UnaPlataforma.getElementsByTagName("Plataforma")

            print("Tamaño Plataformas:", len(Plataformas))
            for Plataforma in Plataformas:
                num = len(Plataformas)
                nombre = Plataforma.getElementsByTagName("nombre")[0]
                codigo =  Plataforma.getElementsByTagName("codigo")[0]
                # mi_plataforma.agregar(Plataforma)
                # print(f"codigo = {codigo.firstChild.data}")
                # print(f"nombre = {nombre.firstChild.data}")
                mi_plataforma.insertar(codigo.firstChild.data, nombre.firstChild.data)


    elem = mi_plataforma.Ordenar2()
    print(mi_plataforma.Impimir())
    print("la cantidad de nodos son: ", elem)
    print("la cantidad de nodos por plataforma son: ", num)

    


    ## PARA ESCRIBIR EL DOCUMENTO XML
    ruta = "/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/Practica1/"
    root = ET.Element("JuegosViejos") #elemento padre
    sub_root = ET.SubElement(root, "ListaPlataformas")

    #Para crear las plataformas
    for i in range(0,num):
        hijo = ET.SubElement(sub_root, "Plataforma")
        ET.SubElement(hijo, "codigo").text = mi_plataforma.BuscarCodigoIndice(i)
        ET.SubElement(hijo, "nombre").text = mi_plataforma.BuscarNombreIndice(i)

    archivo = ET.ElementTree(root)
    ET.indent(archivo, ' ')     ##Para darle formato al document
    archivo.write(ruta+"Ejemplo.xml", "UTF-8", xml_declaration=True)

except Exception as err:
    print("Tipo de error: ", err)


