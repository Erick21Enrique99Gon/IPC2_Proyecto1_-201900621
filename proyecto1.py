import easygui
from xml.dom.minidom import parse 
from listas import listaOrtogonal,NodoListaOrgonal
from piso import piso, lista_ ,Clase_Patron,NodoListaEnlazadaDoble
import graphviz 
from cambios import Cambios
Pisol = lista_()


def leer_archivo():
    ruta = easygui.fileopenbox()
    return ruta

def leer_pisos():
    global Pisol
    
    a = parse(leer_archivo())
    pisos = a.getElementsByTagName("piso")
    for p in pisos:
        nombre = p.getAttribute("nombre")
        R = p.getElementsByTagName("R")[0].firstChild.data
        C = p.getElementsByTagName("C")[0].firstChild.data
        F = p.getElementsByTagName("F")[0].firstChild.data
        S = p.getElementsByTagName("S")[0].firstChild.data
        patrones = p.getElementsByTagName("patrones")[0].getElementsByTagName("patron")
        patrones_arreglo = lista_()
        for pat in patrones:
            patron = pat.firstChild.data
            codigo = pat.getAttribute("codigo")
            l = listaOrtogonal(int(C), int(R))
            l.insertar_i_d_a_r(patron.strip())
            patron_clase = Clase_Patron(codigo, l)
            patrones_arreglo.insertarFinal(patron_clase)
        auxpiso = piso(nombre, R, C, F, S,patrones_arreglo)
        Pisol.insertarFinal(auxpiso)
    Pisol.imprimirListaPisos()
    
def graficar():
    print("Escoger el pisto desado ingresando el nombre")
    Pisol.imprimirListaPisos()
    print("Escribir nombre: ")
    nombre = input()
    piso = Pisol.regresarPiso(nombre)
    if piso != None:
        print("Escoger el patron desado ingresando el nombre")
        piso.imprimirIdentificacion()
        print("Escribir codigo: ")
        codigo = input()
        patron = piso.patrones.regresarPatron(codigo)
        if patron != None:
            print("Patron:")
            patron.listaOrtogonal.imprimir()
            patron.listaOrtogonal.graficar(patron.codigo,piso.nombre)
    
def cambio():
    print("Escoger el pisto desado ingresando el nombre")
    Pisol.imprimirListaPisos()
    print("Escribir nombre: ")
    nombre = input()
    piso = Pisol.regresarPiso(nombre)
    if piso != None:
        print("Escoger el patron inicial")
        piso.imprimirIdentificacion()
        print("Escribir codigo: ")
        codigo = input()
        patronInicial = piso.patrones.regresarPatron(codigo)
        if patronInicial != None:
            print("Patron:")
            patronInicial.listaOrtogonal.imprimir()
            patronInicial.listaOrtogonal.graficar(patronInicial.codigo,piso.nombre)
        print("Escoger el patron final")
        piso.patrones.imprimirListaPatrones()
        print("Escribir codigo: ")
        codigo = input()
        patronFinal = piso.patrones.regresarPatron(codigo)
        if patronFinal != None:
            print("Patron:")
            patronFinal.listaOrtogonal.imprimir()
            patronFinal.listaOrtogonal.graficar(patronFinal.codigo,piso.nombre)
        cambiando = Cambios(piso.S, piso.F)
        cambiando.CAMBIAR(patronInicial, patronFinal)

if __name__ == '__main__':
    llave = True
    
    while(llave):
        print("Escoger una opcion")
        print("1.)Ingresar Archivo")
        print("2.)Graficar")
        print("3.)Cambiar posiciones")
        print("4.)Salir")
        selector = input()
        if selector == "1":
            leer_pisos()
        
        if selector == "2":
            graficar()

        if selector == "3":
            cambio()

        if selector == "4":
            llave = False

