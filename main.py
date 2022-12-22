import Clases
import tkinter as tk
import tkinter.filedialog
from LeerXML import *
from Premiacion import *
from ListaSimple import *
from ListaSimple import colaJugadores
from ListaSimple import pilaPremios

colaJugadores=ListaJugadores()
pilaPremios=ListaSimple()

def cargaJugadores(ruta):
    colaJugadores1=LeerJugadoresXML(ruta)
    print("Se Registrarona los Jugadores:")
    colaJugadores1.recorridoJugadores()
    return colaJugadores1

def cargaPremios(ruta):
    pilaPremios=LeerPremiosXML1(ruta)
    return pilaPremios

def buscarArchivo(textBox):
    textBox.delete("1","end")
    ruta=tk.filedialog.askopenfilename()
    textBox.insert(0,ruta)

def imprimirJugadores(colaJugadores):
    colaJugadores.recorridoJugadores()

def imprimirPremios(pilapremios):
    aux=pilaPremios.primero
    if aux==None:
        print("La pila de regalos esta vacia")
    while aux!=None:
        print("Premio: ", aux.dato)
        aux=aux.next

def empezarPremiacion(rutaJugadores, rutaPremios):
    colaJugadores=LeerJugadoresXML(rutaJugadores)
    pilaPremios=LeerPremiosXML1(rutaPremios)
    celebrarPremiacion(colaJugadores,pilaPremios)

windowMain = tk.Tk()
windowMain.title("Menu Principal") #Asignarle titulo a ala ventana
windowMain.columnconfigure([0,4], minsize=200) #Columnas de la Ventana
windowMain.rowconfigure([0,10], minsize=100) #Filas de la Ventana y su proporción
windowMain.configure(background="#ff6b6b")

label1 = tk.Label(text="Christmas Puzzle", bg="#ff6b6b")
label1.grid(row=0,column=2, pady=10)

label2 = tk.Label(windowMain, text="Ruta y  Nombre del Archivo de Jugadores :" , bg="#ff6b6b")
label2.grid(row=1,column=1, padx=10)

textBox1 = tk.Entry(windowMain, text="",width="75")
textBox1.grid(row=1,column=2, padx=10,pady=10)

label3 = tk.Label(windowMain, text="Ruta y  Nombre del Archivo de Regalos :" , bg="#ff6b6b")
label3.grid(row=2,column=1, padx=10)

textBox2 = tk.Entry(windowMain, text="",width="75")
textBox2.grid(row=2,column=2, padx=10,pady=10)

button1= tk.Button(windowMain, text ="Revisar informacion de Jugadores" ,  command=lambda: cargaJugadores(textBox1.get()) , bg="#6ab04c") #Boton de Cargar Archivo
button1.grid(row=3,column=1, padx=10,pady=10)

button2= tk.Button(windowMain, text ="Revisar informacion de Premios" ,  command=lambda: cargaPremios(textBox2.get()) , bg="#6ab04c") #Boton de Cargar Archivo
button2.grid(row=3,column=3, padx=10,pady=10)

button3= tk.Button(windowMain, text ="Buscar Archivo Jugadores" ,  command=lambda: buscarArchivo(textBox1) , bg="#f9ca24") #Boton de Buscar Archivo Jugadores
button3.grid(row=1,column=3, padx=10,pady=10)

button4= tk.Button(windowMain, text ="Buscar Archivo Premios" ,  command=lambda: buscarArchivo(textBox2) , bg="#f9ca24") #Boton de Buscar Archivo Premios
button4.grid(row=2,column=3, padx=10,pady=10)

button5= tk.Button(windowMain, text ="Imprimir Jugadores" ,  command=lambda: imprimirJugadores(colaJugadores) , bg="#6ab04c") #Boton de Cargar Archivo
button5.grid(row=5,column=1, padx=10,pady=10)

button6= tk.Button(windowMain, text ="Celebrar Premiacion \n  Mejores jugadores" ,  command=lambda: empezarPremiacion(textBox1.get(), textBox2.get()) , bg="#6ab04c") #Boton de Cargar Archivo
button6.grid(row=4,column=2, padx=10,pady=10)

button8= tk.Button(windowMain, text ="Imprimir Premios" ,  command=lambda: imprimirPremios(pilaPremios) , bg="#6ab04c") #Boton de Cargar Archivo
button8.grid(row=5,column=3, padx=10,pady=10)

windowMain.mainloop()               #Llamamos a la ventana