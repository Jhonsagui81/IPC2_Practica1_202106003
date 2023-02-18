import xml.etree.cElementTree as ET 
from xml.dom import minidom
from Plataformas import ListaPlataforma
from Juegos import ListaJuegos


try:
    ## LEEER Y EXTRACCION DE DATOS DEL XML
    doc = minidom.parse("/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/Practica1/salida.xml")

    print("Ya paso")

    ##PARA ACCEDER A PLATAFORMAS
    mi_plataforma = ListaPlataforma()  # Lista de Nodos Plataforma

    JuegosViejos = doc.getElementsByTagName("JuegosViejos")  #accediendo al xml desde la raiz
    print("Tamaño JuegosViejos: ", len(JuegosViejos))
    for JuegoViejo in JuegosViejos:
        ListaPlataformas = JuegoViejo.getElementsByTagName("ListaPlataformas")
        print("Tamaño ListaPlatformas:", len(ListaPlataformas))
        for UnaPlataforma in ListaPlataformas:
            Plataformas = UnaPlataforma.getElementsByTagName("Plataforma")
            print("Tamaño Plataformas:", len(Plataformas))
            for Plataforma in Plataformas:
                num_plataformas = len(Plataformas)
                nombre = Plataforma.getElementsByTagName("nombre")[0]
                codigo =  Plataforma.getElementsByTagName("codigo")[0]
                mi_plataforma.insertar(codigo.firstChild.data, nombre.firstChild.data)


    ##PARA ACCEDER A JUEGOS
    mi_juego = ListaJuegos()    #Lista de Nodos Juegos 

    for JuegoViejo in JuegosViejos:
        ListadoJuegos = JuegoViejo.getElementsByTagName("ListadoJuegos")
        print("Tamanio ListadoJuegos: ", len(ListadoJuegos))
        for UnJuego in ListadoJuegos:
            juego = UnJuego.getElementsByTagName("Juego")
            print("Tamanio Juego: ", len(juego))
            for Juegos in juego:
                num_juegos = len(juego)
                codigo_juego = Juegos.getElementsByTagName("codigo")[0]
                nombre_juego = Juegos.getElementsByTagName("nombre")[0]
                plata1 = Juegos.getElementsByTagName("Plataformas")
                for plarts_externa in plata1:
                    plata2 = plarts_externa.getElementsByTagName("Plataforma")
                    for plat_inter in plata2:
                        codigo_plat = plat_inter.getElementsByTagName("codigo")[0]
                mi_juego.insertar(codigo_juego.firstChild.data, nombre_juego.firstChild.data, codigo_plat.firstChild.data)
                
                    

    #Ordenar la lista de Plataformas
    mi_plataforma.Ordenar2()
    print(mi_plataforma.Impimir())
    print("la cantidad de nodos por plataforma son: ", num_plataformas)

    #Ordenar la lista de Juegos
    mi_juego.Ordenar2()
    print(mi_juego.Impimir())
    print("la cantidad de nodos por Juego son: ", num_juegos)



    ## PARA ESCRIBIR EL DOCUMENTO XML

    ruta = "/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/Practica1/"
    root = ET.Element("JuegosViejos") #elemento padre
    sub_root = ET.SubElement(root, "ListaPlataformas")
    sub_root_1 = ET.SubElement(root, "ListadoJuegos")

    #Para crear las plataformas
    for i in range(0,num_plataformas):
        hijo = ET.SubElement(sub_root, "Plataforma")
        ET.SubElement(hijo, "codigo").text = mi_plataforma.BuscarCodigoIndice(i)
        ET.SubElement(hijo, "nombre").text = mi_plataforma.BuscarNombreIndice(i)

    #Para crear Los juegos
    for ide in range (0,num_juegos):
        hijos = ET.SubElement(sub_root_1,"Juego")
        ET.SubElement(hijos, "codigo").text = mi_juego.BuscarCodigoIndice(ide)
        ET.SubElement(hijos, "nombre").text = mi_juego.BuscarNombreIndice(ide)
        nieto = ET.SubElement(hijos, "Plataformas")
        for sub_plat in plata1:
            sub_nieto = ET.SubElement(nieto, "Plataforma")
            ET.SubElement(sub_nieto, "codigo").text = mi_juego.BuscarCodigoPlatformaIndice(ide)


    archivo = ET.ElementTree(root)
    ET.indent(archivo, ' ')     ##Para darle formato al document
    archivo.write(ruta+"Ejemplo.xml", "UTF-8", xml_declaration=True)

except Exception as err:
    print("Tipo de error: ", err)


