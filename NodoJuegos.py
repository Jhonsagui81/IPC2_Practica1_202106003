class Juego:
    def __init__(self, Codigo, Cadena):
        self.Codigo = Codigo
        self.Cadena = Cadena


class NodoJuegos:
    def __init__(self, Codigo, Cadena):
        self.Dato = Juego(Codigo, Cadena)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerCadena(self):
        return self.Dato.Cadena

    def ObtenerNumero(self):
        return self.Dato.Codigo
    
    def Imprimir(self):
        return str(self.Dato.Codigo) + "-" + str(self.Dato.Cadena)