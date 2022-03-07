import listas 
class piso:
    def __init__(self,nombre:str ,R: int,C:int,F:int,S:int,patrones):
        self.nombre = nombre
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones = patrones
    def imprimirIdentificacion(self):
        print("Nombre: " + self.nombre + " R: "+ str( self.R)+" C: "+ str( self.C)+" F: "+ str( self.F)+" S: "+ str(self.S))
        self.patrones.imprimirListaPatrones()

class Clase_Patron:
    def __init__(self,codigo,listaOrtogonal):
        self.codigo = codigo
        self.listaOrtogonal = listaOrtogonal

class NodoListaEnlazadaDoble:
    def __init__(self,dato):
        self.siguiente = None
        self.anterior = None
        self.dato = dato


class lista_:
    def __init__(self):
        self.inicio = None
        self.final= None
        
    def insertarPrincipio(self,dato):
        nuevoNodo = NodoListaEnlazadaDoble(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.final = nuevoNodo
        else:
            self.inicio.anterior = nuevoNodo
            nuevoNodo.siguiente = self.inicio
            self.inicio = nuevoNodo
    
    def insertarFinal(self, dato):
        nuevoNodo = NodoListaEnlazadaDoble(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.final = nuevoNodo
        else:
            self.final.siguiente = nuevoNodo
            nuevoNodo.anterior = self.final
            self.final = nuevoNodo
    
    def borrarDato(self, dato):
        nodoTemporal=NodoListaEnlazadaDoble("")
        nodoTemporal = self.inicio

        while nodoTemporal != None:
            if nodoTemporal.dato == dato:
                if self.inicio.dato == dato:
                    self.inicio = self.inicio.siguiente
                    nodoTemporal.siguiente = None
                    self.inicio.anterior = None
                if self.final.dato == dato:
                    self.final = self.final.anterior
                    nodoTemporal.anterior = None
                    self.final.siguiente = None
                else:
                    nodoTemporal.anterior.siguiente = nodoTemporal.siguiente
                    nodoTemporal.siguiente.anterior = nodoTemporal.anterior
                    nodoTemporal.siguiente = nodoTemporal.anterior = None
            nodoTemporal = nodoTemporal.siguiente
    
    def regresarPiso(self, nombre):
        nodoTemporal=NodoListaEnlazadaDoble("")
        nodoTemporal = self.inicio

        while nodoTemporal != None:
            if nodoTemporal.dato.nombre == nombre:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        print("No se encontro el piso")
    
    def regresarPatron(self, codigo):
        nodoTemporal=NodoListaEnlazadaDoble("")
        nodoTemporal = self.inicio

        while nodoTemporal != None:
            if nodoTemporal.dato.codigo == codigo:
                return nodoTemporal.dato
            nodoTemporal = nodoTemporal.siguiente
        print("No se encontro el patron")

    def ordenarListaPorNombrePiso(self):
        aux = NodoListaEnlazadaDoble("")
        aux = self.final
        if aux != None:
            while aux != None:
                aux2 = NodoListaEnlazadaDoble("")
                
                if aux.anterior!=None:
                    if aux.dato.nombre < aux.anterior.dato.nombre:
                        aux2.dato = aux.dato
                        aux.dato = aux.anterior.dato
                        aux.anterior.dato = aux2.dato
                aux = aux.anterior
            
    def ordenarListaPorCodigoPatron(self):
        aux = NodoListaEnlazadaDoble("")
        aux = self.final
        if aux != None:
            while aux != None:
                aux2 = NodoListaEnlazadaDoble("")
                
                if aux.anterior!=None:
                    if aux.dato.codigo < aux.anterior.dato.codigo:
                        aux2.dato = aux.dato
                        aux.dato = aux.anterior.dato
                        aux.anterior.dato = aux2.dato
                aux = aux.anterior

    def imprimirListaPisos(self):
        nodoTemp = NodoListaEnlazadaDoble("")
        nodoTemp = self.inicio
        while nodoTemp != None:
            nodoTemp.dato.imprimirIdentificacion()
            nodoTemp = nodoTemp.siguiente
    
    def imprimirListaPatrones(self):
        nodoTemp = NodoListaEnlazadaDoble("")
        nodoTemp = self.inicio
        while nodoTemp != None:
            print("Codigo: "+ nodoTemp.dato.codigo)
            print("Patron: ")
            nodoTemp.dato.listaOrtogonal.imprimir()
            nodoTemp = nodoTemp.siguiente