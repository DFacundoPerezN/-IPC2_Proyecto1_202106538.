import Clases
import tkinter as tk
import tkinter.filedialog
import LeerXML

def cargaJugadores():
    print("Se Registrarona los Jugadores:")

def cargaPremios():
    print("Se Registrarona los Premios:")    

def buscarArchivo():
    ruta=tk.filedialog.askopenfilename()
    textBox1.insert(0,ruta)

windowMain = tk.Tk()
windowMain.title("Menu Principal") #Asignarle titulo a ala ventana
windowMain.columnconfigure([0,4], minsize=200) #Columnas de la Ventana
windowMain.rowconfigure([0,10], minsize=100) #Filas de la Ventana y su proporción
windowMain.configure(background="#ff6b6b")

label1 = tk.Label(text="Christmas Puzzle", bg="#ff6b6b")
label1.grid(row=0,column=2, pady=10)

label2 = tk.Label(windowMain, text="Ruta y  Nombre del Archivo:" , bg="#ff6b6b")
label2.grid(row=1,column=1, padx=10)

textBox1 = tk.Entry(windowMain, text="",width="75")
textBox1.grid(row=1,column=2, padx=10,pady=10)

button1= tk.Button(windowMain, text ="Cargar informacion de Jugadores" ,  command=lambda: cargaJugadores() , bg="#6ab04c") #Boton de Cargar Archivo
button1.grid(row=3,column=1, padx=10,pady=10)

button2= tk.Button(windowMain, text ="Cargar informacion de Premios" ,  command=lambda: cargaPremios() , bg="#6ab04c") #Boton de Cargar Archivo
button2.grid(row=3,column=3, padx=10,pady=10)

button3= tk.Button(windowMain, text ="Buscar Archivo" ,  command=lambda: buscarArchivo() , bg="#f9ca24") #Boton de Buscar Archivo
button3.grid(row=2,column=2, padx=10,pady=10)

windowMain.mainloop()               #Llamamos a la ventana