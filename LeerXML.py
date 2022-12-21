import xml.etree.ElementTree as ET
from xml.dom import minidom
from ClaseNodo import *
from ListaSimple import *
from ClaseCelda import Celda
from Clases import Jugador
from Clases import ImprimirInfo

def LeerJugadoresXML(ruta):
    print("leyendo archivo en ruta: ", ruta)

    tree = ET.parse(ruta)
    root = tree.getroot()  

    listaJugadores = ListaSimple()

    for element in root:
        
        if element.tag == "jugador":
            print("jugador encontrado")
            
            for sub1 in element:
                
                if sub1.tag == "datospersonales":
                    for sub2 in sub1:
                        if sub2.tag == "nombre":
                            nombre = sub2.text.replace("$", "")
                        
                        if sub2.tag == "edad":
                            edad = sub2.text.replace("$", "")

                elif sub1.tag == "movimientos":
                    movimientos = int(sub1.text)

                elif sub1.tag == "tamaño":
                    size = int(sub1.text)

                elif sub1.tag == "figura":
                    figura = sub1.text

                elif sub1.tag == "puzzle":
                    listaPuzzle= ListaSimple()
                    for sub2 in sub1:
                        if sub2.tag == "celda":
                            fila = sub2.attrib['f']
                            columna = sub2.attrib['c']
                            listaPuzzle.agregarUltimo(Celda(fila, columna))
                
                elif sub1.tag == "solucion":
                    listaSolucion= ListaSimple()
                    for sub2 in sub1:
                        if sub2.tag == "celda":
                            fila = sub2.attrib['f']
                            columna = sub2.attrib['c']
                            listaSolucion.agregarUltimo(Celda(fila, columna))        

            jugadorNuevo = Jugador(nombre, edad, movimientos, size, figura, listaPuzzle, listaSolucion)
            ImprimirInfo(jugadorNuevo)
            listaJugadores.agregarUltimo(jugadorNuevo)

    return listaJugadores

def LeerPremiosXML1(ruta):
    pilaRegalos= ListaSimple()

    doc = minidom.parse(ruta)
    regalos = doc.getElementsByTagName("regalo")


    for regalo in regalos:        
        print(regalo.firstChild.data)
        pilaRegalos.agregarPrimero(regalo.firstChild.data)

    temp=pilaRegalos.primero
    while temp!=None:
        print("Premio: ",temp.dato)
        temp=temp.next

    return pilaRegalos

def AbrirXML():
    tree = ET.parse('Entrada.xml')
    root = tree.getroot()

    for element in root:
        print(element.tag)

#LeerJugadoresXML('Entrada.xml')
#AbrirXML()

#LeerPremiosXML1("Premios.xml")