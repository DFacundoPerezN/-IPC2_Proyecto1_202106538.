from Clases import Jugador
from ClaseNodo import Nodo

class ListaSimple():
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def estaVacia(self):
        return self.primero==None

    def agregarPrimero(self,dato): #Pila
        
        new=Nodo(dato)

        if self.primero==None:
            self.primero=self.ultimo=new
        else:
            temp = new
            temp.next = self.primero
            self.primero = temp

    def agregarUltimo(self,dato):  #Cola

        new=Nodo(dato)
        temp = self.primero

        if self.primero==None:
            print("Estaba vacia")
            self.primero=self.ultimo=new
        else:
            temp=self.primero
            while temp.next is not None:
                temp=temp.next

            self.ultimo=new
            new.before=temp
            temp.next=new

    def sacarPrimero(self): #Cola Y Pila
        tmp=self.primero

        if tmp==None:
            print("la lista esta vacia")
            return tmp

        elif tmp.next == None:
            print("solo hay uno en la cola")
            self.primero=None
            self.ultimo=None
            return tmp

        else:
            self.primero=tmp.next
            tmp.next.before=None
            return tmp          #Devuelve el nodo

    def sacarUltimo(self):
        tmp= self.primero

        if tmp==None:
            print("la lista esta vacia")
            return tmp

        elif tmp.next == None:
            print("solo hay uno en la cola")
            self.primero=None
            return tmp

        else:
            while tmp.next is not None:
                tmp=tmp.next
            tmp.before.next=None
            return tmp

    def cantidad(self):
        tmp = self.primero
        cantidad=0
        while tmp is not None:
            tmp=tmp.next
            cantidad+=1
        return cantidad

    def recorridoJugadores(self):
        temp=self.primero
        if temp is None:
            print("esta vacia")
        while temp!=None:
            print("Nombre: ", temp.dato.nombre, ", Edad: ", temp.dato.edad, ", Puntos: ", temp.dato.puntos)
            temp=temp.next
        

class ListaJugadores(ListaSimple):
    def __init__(self):
        super().__init__()
    
    def agregarOrdenado(self, dato):
        new=Nodo(dato)
        temp = self.primero

        if temp==None:
            self.primero=self.ultimo=new

        else:
            
            if dato.puntos <= self.primero.dato.puntos :
                new.next=self.primero
                self.primero.before=new
                self.primero=new
                
            elif dato.puntos > self.ultimo.dato.puntos:
                self.ultimo.next = new
                new.before=self.ultimo
                self.ultimo=new

            else:
                while temp.next is not None:
                    jugador =temp.dato
                    if dato.puntos <= jugador.puntos:
                        new.next=temp
                        new.before=temp.before
                        temp.before.next=new
                        temp.before=new
                        break
                    elif dato.puntos > jugador.puntos:
                        temp=temp.next
                    else:
                        break

    def Top10(self):
        top10=ListaSimple()
        temp=self.ultimo
        c=0
        while c<10:
            if temp!=None:
                print("#",c+1 , temp.dato.nombre, " puntuacion: ", temp.dato.puntos)
                top10.agregarPrimero(temp.dato)
                temp=temp.before
            c+=1
        return top10

colaJugadores=ListaJugadores()
pilaPremios=ListaSimple()

'''pruebaJugadores = ListaJugadores()
lui=Jugador("Lui", 25, 20, 20, "arbol", None, None)
pruebaJugadores.agregarOrdenado(lui)
mano=Jugador("Mano", 24, 16, 25, "arbol", None, None)
pruebaJugadores.agregarOrdenado(mano)
pruebaJugadores.agregarOrdenado(Jugador("Jorge", 35, 15, 30, "arbol", None, None))
pruebaJugadores.agregarOrdenado(Jugador("Jusep", 35, 40, 5, "arbol", None, None))
pruebaJugadores.agregarOrdenado(Jugador("Geron", 35, 26, 25, "arbol", None, None))
pruebaJugadores.agregarOrdenado(Jugador("Sael", 5, 22, 20, "arbol", None, None))
doom=Jugador("Doom", 35, 21, 15, "arbol", None, None)
pruebaJugadores.agregarOrdenado(doom)
pruebaJugadores.agregarOrdenado(Jugador("Junker", 35, 16, 20, "arbol", None, None))
pruebaJugadores.recorridoJugadores()
top10J=pruebaJugadores.Top10()
top10J.recorridoJugadores()'''
