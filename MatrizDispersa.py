from Nodo_Encabezado import NodoEncabezado
from Lista_Encabezado import ListaEncabezado
import os

class Nodo_Interno():
    def __init__(self,x,y, caracter):
        self.caracter = caracter
        self.coordenadaX=x
        self.coordenadaY=y

        self.arriba=None
        self.abajo=None
        self.derecha=None
        self.izquierda=None

class MatrizDispersa():
    def __init__(self,capa):
        self.capa=capa
        self.filas= ListaEncabezado('fila')
        self.columnas= ListaEncabezado('columna')

    def insert(self, posX, posY, caracter):
        nuevo = Nodo_Interno(posX, posY, caracter)
        nodoX= self.filas.getEncabezado(posX)
        nodoY = self.columnas.getEncabezado(posY)
    
        if nodoX == None:
            nodoX=NodoEncabezado(posX)
            self.filas.insertar_nodoEncabezado(nodoX)

        if nodoY == None:
            nodoY=NodoEncabezado(posY)
            self.filas.insertar_nodoEncabezado(nodoY)

        #insertar nuevo en la fila cuando ya existen nodos en la fila

        if nodoX.acceso==None:
            nodoX.acceso=nuevo
        else:
            if nuevo.coordenadaX< nodoX.acceso.coordenadaY:
                nuevo.derecha=nodoX.acceso
                nodoX.acceso.izquierda=nuevo
                nodoX.acceso=nuevo
            else:
                tmp : Nodo_Interno = nodoX.acceso
                while tmp != None:
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha= tmp
                        nuevo.izquierda= tmp.izquierda
                        tmp.izquierda.derecha= nuevo
                        tmp.izquierda=nuevo
                        break
                    elif nuevo.coordenadaX==tmp.coordenadaX and nuevo.coordenadaY==tmp.coordenadaY:
                        break
                    else:
                        if tmp.derecha==None:
                            tmp.derecha=nuevo
                            nuevo.izquierda=tmp
                            break
                        else:
                            tmp= tmp.derecha
        if nodoY.acceso==None:
            nodoY.acceso=nuevo
        else:
            if nuevo.coordenadaX < nodoY.acceso.coordenadaX:
                nuevo.abajo=nodoX.acceso
                nodoY.acceso.arriba=nuevo
                nodoY.acceso= nuevo
            else:
                tmp2: Nodo_Interno=nodoY.acceso
                while tmp2!=None:
                    if nuevo.coordenadaY<tmp2.coordenadaY:
                        nuevo.abajo=tmp
                        nuevo.arriba=tmp.arriba
                        tmp2.arriba.abajo=nuevo
                        tmp2.arriba=nuevo
                        break

                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY==tmp2.coordenadaY:
                        break
                    else:
                        if tmp2.abajo==None:
                            tmp2.abajo=nuevo
                            nuevo.arriba=tmp2
                            break
                        else:
                            tmp2=tmp2.abajo

    def graficarDibujo(self, nombre):
        contenido=''
        contenido+='\ndiagraph G{ \n'
        contenido+='\nnode[shape=box, width=0.7, height=0.7, fontname=\" Century Gothic\", fillcolor=\"white\", style=filled] \n'
        contenido+='\nedge[style="bold"] \n'
        contenido+='\nnode[label="capa:'+str(self.capa) +' fillcolor="red" pos="-1,1!]'
        contenido+='\nlabel="{}" \n fontname="Arial Black" \n fontsize="25pt" \n '.format('\n Matriz Dispersa')

        pivote=self.filas.primero
        posx=0
        while pivote!=None:
            contenido+='\n\t node[label="F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{}; '.format(pivote.id,posx,pivote.siguiente.id)
            pivote=pivote.siguiente
            posx+=1
        pivote=self.filas.primero
        while pivote.siguiente != None:
            contenido+= '\n\t x{}->x{}; '.format(pivote.id,pivote.siguiente.id)
            contenido+= '\n\t x{}->x{}[dir=black]; '.format(pivote.id,pivote.siguiente.id)
            pivote=pivote.siguiente
        contenido+='\n \t raiz->x{};' .format(self.filas.primero.id)

        pivotey=self.columnas.primero
        posy=0
        while pivotey!=None:
            contenido+='\n\t node [label="C{}" fillclor="azure3" por="{},1!" dhape=box]y{};' .format(pivotey.id, pivotey.siguiente.id)
            contenido+='\n\t node [label="C{}" fillclor="azure3" por="{},1!" dhape=box]y{};' .format(pivotey.id, pivotey.siguiente.id)
            pivotey=pivotey.siguiente
            posy+=1
        pivotey=self.columnas.primero
        while pivotey.siguiente!=None:
            contenido+='\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)