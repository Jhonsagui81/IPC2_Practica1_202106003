import xml.etree.cElementTree as ET 
from xml.dom import minidom
from acceso import *

## LEEER Y EXTRACCION DE DATOS DEL XML

print("Infrese la direccion del documento: ")
# entrada = input()
doc = minidom.parse("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/Practica1/salida.xml")

print("Ya paso")


print("-----------Acceso global-----------")
JuegosViejos = doc.getElementsByTagName("JuegosViejos")
ListaPlataformas = doc.getElementsByTagName("Plataforma")

for Plataforma in ListaPlataformas:
    print(HijosATexto(Plataforma))
    
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
            print(HijosATexto(Plataforma))


##     ESCRITURA DEL XML

