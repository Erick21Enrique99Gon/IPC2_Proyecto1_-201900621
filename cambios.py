from listas import*
from piso import*
class cambios_de_patron:
    def __init__(self,precio,lista_de_cambios):
        self.precio = precio
        self.lista_de_cambios = lista_de_cambios

class Cambios:
    def __init__(self,S,F):
        self.F = int(F)
        self.S = int(S)
        self.lista_de_precios = lista()
    
    def CAMBIAR(self,patronInicial,patronFinal):
        auxPI = listaOrtogonal(0, 0)
        auxPI= patronInicial.listaOrtogonal
        auxPF = listaOrtogonal(0, 0)
        auxPF= patronFinal.listaOrtogonal
        nodoaux1PI = NodoListaOrgonal("")
        nodoaux1PF = NodoListaOrgonal("")
        precio = 0
        contador=1
        if auxPI.cabeza != None and auxPF.cabeza !=None:
            aux_lista_cambios=lista()
            nodoaux2PF = auxPF.cabeza
            nodoaux2PI = auxPI.cabeza
            while nodoaux2PF != None and nodoaux2PI != None:
                nodoaux1PF = nodoaux2PF
                nodoaux1PI = nodoaux2PI
                while nodoaux1PF != None and nodoaux1PI!= None:
                    if nodoaux1PF.dato != nodoaux1PI.dato:
                       nodoaux1PI.dato = nodoaux1PF.dato
                       print(str(contador)+".) Se volteo el azulejo en la fila "+str(nodoaux1PI.ubicaciony)+" column a "+ str(nodoaux1PI.ubicacionx) )
                       auxPI.imprimir()
                       precio += self.F
                       aux_lista_cambios.insertarFinal(auxPI)
                       contador = contador +1 
                    nodoaux1PF = nodoaux1PF.siguiente
                    nodoaux1PI = nodoaux1PI.siguiente
                nodoaux2PF = nodoaux2PF.abajo
                nodoaux2PI = nodoaux2PI.abajo
            
            self.lista_de_precios.insertarFinal(cambios_de_patron(precio, aux_lista_cambios))
            print("El total con el metodo es de: Q"+ str(precio+".00"))
            
            '''auxPI= patronInicial.listaOrtogonal
            nodoaux2PF = auxPF.cabeza
            nodoaux2PI = auxPI.cabeza
            while nodoaux2PF != None and nodoaux2PI != None:
                nodoaux1PF = nodoaux2PF
                nodoaux1PI = nodoaux2PI
                while nodoaux1PF != None and nodoaux1PI!= None:
                    if nodoaux1PF.dato != nodoaux1PI.dato:
                        if nodoaux1PI.siguiente != nodoaux1PF.siguiente:

                            precio += self.F
                    nodoaux1PF = nodoaux1PF.siguiente
                    nodoaux1PI = nodoaux1PI.siguiente
                nodoaux2PF = nodoaux2PF.abajo
                nodoaux2PI = nodoaux2PI.abajo
            
            nodoaux2PF = auxPF.cabeza
            nodoaux2PI = auxPI.cabeza
            while nodoaux2PF != None and nodoaux2PI != None:
                nodoaux1PF = nodoaux2PF
                nodoaux1PI = nodoaux2PI
                while nodoaux1PF != None and nodoaux1PI!= None:
                    if nodoaux1PF.dato != nodoaux1PI.dato:
                       nodoaux1PI.dato = nodoaux1PF.dato
                       precio += self.F
                    nodoaux1PF = nodoaux1PF.siguiente
                    nodoaux1PI = nodoaux1PI.siguiente
                nodoaux2PF = nodoaux2PF.abajo
                nodoaux2PI = nodoaux2PI.abajo
            
            self.lista_de_precios.insertarFinal(str(precio))'''