from Clases import *
from ClaseNodo import Nodo

class ListaSimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        return self.primero==None

    def agregarPrimero(self,dato): #Pila
        
        new=Nodo(dato)

        if self.estaVacia:
            self.primero=self.ultimo=new
        else:
            temp = new
            temp.next = self.primero
            self.primero = temp

    def agregarUltimo(self,dato):  #Cola

        new=Nodo(dato)
        temp = self.primero

        if self.estaVacia:
            self.primero=self.ultimo=new
        else:
            temp=self.primero
            while temp.next is not None:
                temp=temp.next
            temp.next=new

    def recorridoJugadores(self):
        temp=self.primero
        while temp!=None:
            print("Nombre: ", temp.dato.nombre, ", Edad: ", temp.dato.edad)
            temp=temp.next