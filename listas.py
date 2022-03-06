import webbrowser
import graphviz 
class NodoListaOrgonal:
    def __init__(self,dato:str):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.arriba = None
        self.abajo = None
        self.ubicacionx = 0
        self.ubicaciony = 0
    
class NodoListaEnlazadaDoble:
    def __init__(self,dato):
        self.ubicacion = 0
        self.siguiente = None
        self.anterior = None
        self.dato = dato

class lista:
    def __init__(self):
        self.inicio = None
        self.final= None
        self.ubicacion = 0
        
    
    def insertarPrincipio(self,dato:str):
        nuevoNodo = NodoListaEnlazadaDoble(dato)
        if self.inicio == None:
            self.inicio = nuevoNodo
            self.final = nuevoNodo
        else:
            self.inicio.anterior = nuevoNodo
            nuevoNodo.siguiente = self.inicio
            self.inicio = nuevoNodo
    
    def insertarFinal(self,dato):
        nuevoNodo = NodoListaEnlazadaDoble(dato)
        if self.inicio == None:
            self.ubicacion = 1
            nuevoNodo.ubicacion = self.ubicacion
            self.inicio = nuevoNodo
            self.final = nuevoNodo

        else:
            self.ubicacion += 1
            nuevoNodo.ubicacion = self.ubicacion
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

    def imprimirLista(self):
        nodoTemp = NodoListaEnlazadaDoble("")
        nodoTemp = self.inicio
        while nodoTemp != None:
            print("nodo: " + nodoTemp.dato)
            nodoTemp = nodoTemp.siguiente
    
    def ordenarListaPorPrecios(self):
        nodoTemp = NodoListaEnlazadaDoble("")
        nodoTemp = self.inicio
        while nodoTemp != None:
            print("nodo: " + nodoTemp.dato)
            nodoTemp = nodoTemp.siguiente

class listaOrtogonal:
    def __init__(self,lx:int,ly:int):
        self.cabeza = None
        self.final = None
        self.listax = lista()
        self.listay = lista()
        self.lx = lx
        self.ly = ly

    
    def insertar_i_d_a_r(self,dato):
        nodoaux1 = NodoListaOrgonal("")
        nodoaux2 = NodoListaOrgonal("")
        contador = 0
        color =dato
        for y in range(self.ly):
            for x in range(self.lx):
                nuevo = NodoListaOrgonal(color[contador])
                nuevo.ubicacionx = x
                nuevo.ubicaciony = y
                if x == 0:
                    if self.cabeza == None:
                        self.cabeza = nuevo
                    nodoaux1 =nuevo
                elif nodoaux1 ==None:
                    pass        
                else:
                    nuevo.anterior = nodoaux1
                    nodoaux1.siguiente = nuevo
                    nodoaux1 = nuevo
                    
                if y == 0:
                    nodoaux1 =nuevo
                elif nodoaux2 ==None:
                    pass
                else:
                    nuevo.arriba = nodoaux2
                    nodoaux2.abajo = nuevo
                    nodoaux2 = nodoaux2.siguiente
                    
                contador=contador+1

            nodoaux2 = self.cabeza
            while(nodoaux2.abajo != None):
                nodoaux2 = nodoaux2.abajo
        
    def imprimir(self):
        nodoaux2 = NodoListaOrgonal("")
        if self.cabeza != None:
            nodoaux1 = self.cabeza
            for r in range(self.lx):
                print("--",end="")
            print("-")
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                while(nodoaux2!=None):
                    print("-",end="")
                    print(nodoaux2.dato,end="")
                    nodoaux2 = nodoaux2.siguiente
                print("-")
                for r in range(self.lx):
                    print("--",end="")
                print("-")
                nodoaux1 = nodoaux1.abajo
    
    def graficar(self,codigo:str,nombredePiso:str):
        dot = graphviz.Digraph("Grafica de "+ codigo+" del piso "+ nombredePiso)
        nodoaux2 = NodoListaOrgonal("")
        dot.attr('node',shape = 'square')
        if self.cabeza !=None:
            nodoaux1 = self.cabeza
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                with dot.subgraph() as s:
                    while(nodoaux2!=None):
                        s.attr(rank='same')
                        s.node('('+str(nodoaux2.ubicacionx)+','+ str(nodoaux2.ubicaciony)+')',nodoaux2.dato)
                    
                        nodoaux2 = nodoaux2.siguiente
                    nodoaux1 = nodoaux1.abajo
            
            nodoaux1 = self.cabeza
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                while(nodoaux2!=None):
                    if nodoaux2.abajo != None:
                        dot.edge('('+str(nodoaux2.ubicacionx)+','+ str(nodoaux2.ubicaciony)+')',  '('+str(nodoaux2.abajo.ubicacionx)+','+ str(nodoaux2.abajo.ubicaciony)+')')
                    nodoaux2 = nodoaux2.siguiente
                nodoaux1 = nodoaux1.abajo
            
            nodoaux1 = self.cabeza
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                while(nodoaux2!=None):
                    if nodoaux2.siguiente!= None:
                        dot.edge('('+str(nodoaux2.ubicacionx)+','+ str(nodoaux2.ubicaciony)+')',  '('+str(nodoaux2.siguiente.ubicacionx)+','+ str(nodoaux2.siguiente.ubicaciony)+')')
                    nodoaux2 = nodoaux2.siguiente
                nodoaux1 = nodoaux1.abajo
            
            nodoaux1 = self.cabeza
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                while(nodoaux2!=None):
                    if nodoaux2.arriba != None:
                        dot.edge('('+str(nodoaux2.ubicacionx)+','+ str(nodoaux2.ubicaciony)+')',  '('+str(nodoaux2.arriba.ubicacionx)+','+ str(nodoaux2.arriba.ubicaciony)+')')
                    
                    nodoaux2 = nodoaux2.siguiente
                nodoaux1 = nodoaux1.abajo
            
            nodoaux1 = self.cabeza
            while(nodoaux1 != None):
                nodoaux2 = nodoaux1
                while(nodoaux2!=None):
                    if nodoaux2.anterior != None:
                        dot.edge('('+str(nodoaux2.ubicacionx)+','+ str(nodoaux2.ubicaciony)+')',  '('+str(nodoaux2.anterior.ubicacionx)+','+ str(nodoaux2.anterior.ubicaciony)+')')
                    
                    nodoaux2 = nodoaux2.siguiente
                nodoaux1 = nodoaux1.abajo
        
        dot.render().replace('\\', '/')
        'Grafica.pdf'+ codigo+" del piso "+ nombredePiso