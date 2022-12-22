from ListaSimple import *
from Graficaciones import *

def celebrarPremiacion(listaJugadores:ListaJugadores, pilaPremios:ListaSimple):
    
    top10=listaJugadores.Top10()

    if top10.cantidad() > pilaPremios.cantidad():
        d=top10.cantidad()-pilaPremios.cantidad()
        while d>0:
            top10.sacarPrimero()
            d=top10.cantidad()-pilaPremios.cantidad()

    elif pilaPremios.cantidad() > top10.cantidad():
        d=pilaPremios.cantidad()-top10.cantidad()
        while d>0:
            pilaPremios.sacarUltimo()
            d=pilaPremios.cantidad()-top10.cantidad()

    while (pilaPremios.primero is not None) and (top10.primero is not None):
        jugadorPremiado=top10.sacarPrimero()
        premio=pilaPremios.sacarPrimero()


        print("\n ¡¡¡¡¡ ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")
        print("Felicidades al jugador: ", jugadorPremiado.dato.nombre, " se lleva de regalo: ", premio.dato)
        print(" ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ !!!!!!\n")
        
        crearGraficaPremios(pilaPremios)
        print("se creo grafica de pila de regalos")
        crearGraficaJugadores(listaJugadores)

        input("presione Enter para continuar")

    print("La premiacion llego a su fin xd")



