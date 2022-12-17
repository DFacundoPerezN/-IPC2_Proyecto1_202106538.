class Nodo:

    def __init__(self, dato=None):

        self.dato = dato            #informacion dentro del nodo
        self.next = None            #Apuntador siguiente
        self.before = None          #Apuntador anteiror
        self.up = None
        self.down= None