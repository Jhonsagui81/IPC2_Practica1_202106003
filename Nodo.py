import xml
class Plataforma:
    def __init__(self, Codigo, Cadena):
        self.Codigo = Codigo
        self.Cadena = Cadena


class NodoPlataformas:
    def __init__(self, Codigo, Cadena):
        self.Dato = Plataforma(Codigo, Cadena)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerCadena(self):
        return self.Dato.Cadena

    def ObtenerCodigo(self):
        return self.Dato.Codigo
    
    def Imprimir(self):
        return str(self.Dato.Codigo) + "-" + str(self.Dato.Cadena)