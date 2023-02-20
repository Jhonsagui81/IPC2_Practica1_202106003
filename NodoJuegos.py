class Juego:
    def __init__(self, Codigo, Cadena, Plataforma):
        self.Codigo = Codigo
        self.Cadena = Cadena
        self.Plataforma = Plataforma


class NodoJuegos:
    def __init__(self, Codigo, Cadena, Plataforma):
        self.Dato = Juego(Codigo, Cadena, Plataforma)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerCadena(self):
        return self.Dato.Cadena

    def ObtenerCodigo(self):
        return self.Dato.Codigo
    
    def ObtenerPlataforma(self):
        return self.Dato.Plataforma
    
    def Imprimir(self):
        return str(self.Dato.Codigo) + "-" + str(self.Dato.Cadena)