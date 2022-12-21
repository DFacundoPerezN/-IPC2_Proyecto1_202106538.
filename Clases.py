
def verificarMatriz(size):
    if(-1<size<31 and size%5==0):
        return True
    else:
        return False

def verificarMovs(movimientos):
    if(-1<movimientos<10000):
        return True
    else:
        return False

def conteoPuntos(dimension,movimientos,figura):
    puntos=int(dimension)*5 #sumar puntos en base a la dimension de la matriz, 5 puntos por dimension

    if(movimientos<5):
        puntos=puntos+100
    elif(movimientos<10):
        puntos=puntos+75
    elif(movimientos<15):
        puntos=puntos+50
    elif(movimientos<20):
        puntos=puntos+25
    
    if(figura.find("rbol") or figura.find("Tree")):
        puntos=puntos+250
    elif(figura.find("strella") or figura.find("Star")):
        puntos=puntos+500
    elif(figura.find("egalo") or figura.find("Gift")):
        puntos=puntos+100
    else:
        print("Figura no conocida no se dara puntos por esta")

    return puntos

class Jugador:

    def __init__(self,nombre,edad,moves, size, figura, puzzle, solucion):
        if(verificarMatriz(size) and verificarMovs(moves)):
            self.nombre=nombre
            self.edad= edad
            self.movimientos=moves
            self.size=size
            self.figura=figura
            self.puzzle= puzzle     #podria ser una lista con las celdas marcadas
            self.solucion = solucion    #tambien podria ser una lista conlas celdas
            self.puntos=conteoPuntos(size,moves,figura)

        elif(verificarMatriz(size)):
            print("El numero de movimientos no  debe ser mayor a 10000")
        else:
            print("Tamaño de matriz no valido, debe ser multiplo de 5 y maximo de 30 x 30")


def ImprimirInfo(jugador):
    try:
        print("--------------------------------------------------------------------------------------------------------")
        print("Nombre: ", jugador.nombre, ", Edad: ", jugador.edad, ", Movimientos realizados: ", jugador.movimientos, ", Tamaño del puzzle: ", jugador.size, ", Figura: ", jugador.figura)
    except:
        print("Error en la informacion del jugador")

'''mar=Jugador("Mariano",13,5000,25,"arbol", 24,24)
print((mar.puntos))'''
