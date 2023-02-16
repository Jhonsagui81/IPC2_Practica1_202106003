import Nodo
class ListaJuegos:
    def __init__(self):
        self.cabeza = None
    
    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self, item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    
    def tamanio(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
            
        print(contador)
    
    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
                print(item)
            else:
                actual = actual.obtenerSiguiente()
        return encontrado