from Nodo import NodoPlataformas

class ListaPlataforma:
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Limite = 0 
    
    def insertar(self, Codigo, Nombre):
        NuevoNodo= NodoPlataformas(Codigo,Nombre)
        self.Limite += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def BuscarCodigoIndice(self, posicion):
        if self.Inicio == None:
            return None
        if posicion >= self.Limite:
            #Posicion es mayor al numero de nodos
            return None
        Auxiliar = self.Inicio  ##Posible no se usen
        Previo = None
        if posicion == 0:
            #si la posicion es la inicial
            return Auxiliar.ObtenerCodigo()
        Contador = 0
        while Auxiliar != None:
            if Contador == posicion:
                return Auxiliar.ObtenerCodigo()
            Auxiliar = Auxiliar.Siguiente
            Contador += 1

    def BuscarNombreIndice(self, posicion):
        if self.Inicio == None:
            return None
        if posicion >= self.Limite:
            #Posicion es mayor al numero de nodos
            return None
        Auxiliar = self.Inicio  
        if posicion == 0:
            #si la posicion es la inicial
            return Auxiliar.ObtenerCadena()
        Contador = 0
        while Auxiliar != None:
            if Contador == posicion:
                return Auxiliar.ObtenerCadena()
            Auxiliar = Auxiliar.Siguiente
            Contador += 1        

    def OrdenarElementos(self):
        Bandera = True
        numero = 1
        while Bandera:
            Actual = self.Inicio
            Anterior = None
            Bandera = False
            print("iteracion",numero)
            numero += 1
            while Actual != None:
                if Actual.Siguiente != None:
                    if Actual.ObtenerCodigo() > Actual.Siguiente.ObtenerCodigo():
                        #Si entramos acá, quiere decir que el siguiente nodo es menor al actual
                        Bandera = True
                        if Actual == self.Inicio:
                            #Si entramos acá quiere decir que el elemento desordenado es el primero
                            self.Inicio = Actual.Siguiente
                            Actual.Siguiente = self.Inicio.Siguiente
                            self.Inicio.Siguiente = Actual
                        else:
                            #Si entramos acá quiere decir que el elemento desordenado no es el primero
                            Anterior.Siguiente = Actual.Siguiente
                            Actual.Siguiente = Actual.Siguiente.Siguiente
                            Anterior.Siguiente.Siguiente = Actual
                Anterior = Actual
                Actual = Actual.Siguiente
        return numero