from ListaSimple import*
import os

def textoGraficaJugadores(listajugadores:ListaSimple):
    text=" digraph Jugadores{ \n\n"
    text+=" subgraph cluster_0 { \n\n\t"
    text+=" style=filled; \n\t color=tomato;\n\n\t"
    text+=" node [style=filled,color=lightgoldenrod1, shape=\"septagon\"];\n\t "

    aux=listajugadores.primero
    while aux!=None:
        text+=str(aux.dato.nombre).replace(" ","_")+" \n\t "
        aux=aux.next
    text+="} \n}"
    return text

def crearGraficaJugadores(listaJugadores):
    try:
        file= open('Graficas_Ordenes/JugadoresGrafica.txt', 'w')
    except:
        os.mkdir('Graficas_Ordenes')
        file= open('Graficas_Ordenes/JugadoresGrafica.txt', 'w')
    
    contenido=textoGraficaJugadores(listaJugadores)
    file.write(contenido)
    file.close()
    os.system("dot -Tpng Graficas_Ordenes/JugadoresGrafica.txt -o Graficas_Ordenes/JugadoresGrafica.png")
    os.system("dot -Tpdf Graficas_Ordenes/JugadoresGrafica.txt -o Graficas_Ordenes/JugadoresGrafica.pdf")


def textoGraficaPremios(pilaPremios: ListaSimple):
    text=" digraph P{ \n\n"
    text+=" subgraph cluster_0 { \n\t"
    text+=" style=filled; \n\t color=palegreen2;\n\n\t"
    text+=" Pila[color=\"tomato\" shape=\"record\"    label=\"{"

    aux=pilaPremios.primero
    if aux==None:
        print("La pila esta vacia")
    while aux!=None:
        text+=str(aux.dato)
        if aux.next!=None:
            text+="|"
        aux=aux.next

    text+="}\" ] \n\n\t"
    text+="} \n}"
    return text

def crearGraficaPremios(pilaPremios):
    try:
        file= open('Graficas_Ordenes/PremiosGrafica.txt', 'w')
    except:
        os.mkdir('Graficas_Ordenes')
        file= open('Graficas_Ordenes/PremiosGrafica.txt', 'w')
    
    contenido=textoGraficaPremios(pilaPremios)
    file.write(contenido)
    file.close()
    os.system("dot -Tpng Graficas_Ordenes/PremiosGrafica.txt -o Graficas_Ordenes/PremiosGrafica.png")
    os.system("dot -Tpdf Graficas_Ordenes/PremiosGrafica.txt -o Graficas_Ordenes/PremiosGrafica.pdf")


def graficarPuzzleySolucion(jugador: Jugador):
    nombre=jugador.nombre
    size=jugador.size
    listaCeldasPuzzle:ListaSimple =jugador.puzzle
    listaCeldasSolucion =jugador.solucion

    graficarMatriz(listaCeldasPuzzle, size, nombre, "Puzzle")
    graficarMatriz(listaCeldasSolucion, size, nombre, "Solucion")
    

def graficarMatriz(listaCeldas:ListaSimple, size, nombre, tipo):
    text='digraph MatrizPuzzle{ \n \n   node [shape=record ];\n'
    text+='\t nodesep=0.1; \n\t ranksep = 0;\n\n'

    for fila in range(0,size):
        text+='\t { rank=same '
        for columna in range(0,size):
            celdaLlena=False

            aux=listaCeldas.primero
            while aux!= None:
                if (int(aux.dato.fila)==fila) and (int(aux.dato.columna)==columna):
                    celdaLlena=True
                #print("fila y columna del nodo del nodo: " +str(fila))
                aux=aux.next
            text+='n'+str(columna)+str(fila)+'[label=""'

            if celdaLlena:
                text+=' style=filled color=darkolivegreen4'
            text+='] '
        text+='}\n '

    for i in range(0,size-1):
       text+='\t n0'+str(i)+' -> n0'+str(i+1)+' [arrowhead="none"]\n'
    text+='}'

    try:
        file= open('Matrices/Graficas_'+nombre+'/Matriz'+tipo+'.txt', 'w')
    except:
        try:
            os.mkdir('Matrices/Graficas_'+nombre)
        except:
            os.mkdir('Matrices')
            os.mkdir('Matrices/Graficas_'+nombre)
        file= open('Matrices/Graficas_'+nombre+'/Matriz'+tipo+'.txt', 'w')
    
    file.write(text)
    file.close()
    os.system("dot -Tpng Matrices/Graficas_"+nombre+"/Matriz"+tipo+".txt -o Matrices/Graficas_"+nombre+"/Matriz"+tipo+".png")
    os.system("dot -Tpdf Matrices/Graficas_"+nombre+"/Matriz"+tipo+".txt -o Matrices/Graficas_"+nombre+"/Matriz"+tipo+".pdf")