import numpy as np
from nodo import Nodo

# caballo1 -> 1 -> machine
# caballo2 -> 2 -> humanoide
DIRECCIONES = ["A", "B", "C", "D", "E", "F", "G", "H"]

class Horse:

    def __init__(self, mundo, coordenadas_maquina, coordenadas_humano, tipo_jugador, total_puntos) -> None:
        self.mundo = np.array(mundo)
        self.mundo_aux = self.mundo.copy()
        self.tipo_jugador = tipo_jugador
        self.total_puntos = total_puntos
        self.coordenadas_maquina = coordenadas_maquina
        self.coordenadas_humano = coordenadas_humano
        self.coordenadas = coordenadas_maquina # coordenadas del caballo en turno
        self.nuevos_movimientos = [] # esta lista cambia en el tiempo
        self.direcciones = {}
        #self.posibles_movimientos = [] # una vez definida no se cambia
        self.padre = None
        self.start = False
        self.x = 0
        self.y = 0

# [nodo1, nodo2, nodo3, nodo4]
# [ [ [nodo1, nodo2, nodo3], nodo2, nodo3, nodo4] ]
    
    def movimientos(self) -> list:
        if self.start:
            print(self.padre)
            self.mundo_aux = self.padre.mundo.copy()
            if not self.padre.padre is None:
                #print(self.tipo_jugador)
                #print("Coor:", (self.padre.padre.coordenadas[0], self.padre.padre.coordenadas[1]))
                #exit()
                self.coordenadas = (self.padre.padre.coordenadas[0], self.padre.padre.coordenadas[1])
        else: self.start = True

        self.nuevas_direcciones()
        lista_movimientos = []

        for i in range(8):
            if self.verifica_movimiento(self.direcciones[DIRECCIONES[i]] ):
                self.x = self.direcciones[DIRECCIONES[i]][0]
                self.y = self.direcciones[DIRECCIONES[i]][1]
                utilidad = self.mundo_aux[self.x][self.y]

                #self.mundo_aux[self.coordenadas[0]][self.coordenadas[1]] = 0
                #nuevo_mundo_aux = np.array([])
                nuevo_mundo_aux = self.mundo_aux.copy() 
                nuevo_mundo_aux[self.coordenadas[0]][self.coordenadas[1]] = 0
                nuevo_mundo_aux[self.x][self.y] = self.tipo_jugador

                #self.mundo_aux[x][y] = self.tipo_jugador
                #print(f"Jugador: {self.tipo_jugador}")

                new_nodo = Nodo(nuevo_mundo_aux, self.direcciones[DIRECCIONES[i]], utilidad, self.padre)
                

                lista_movimientos.append(new_nodo)
        print("LISTA:", lista_movimientos)
        return np.array(lista_movimientos)
        


    def verifica_movimiento(self, nueva_coordenada) -> bool:
        if (nueva_coordenada[0] >= 0 and nueva_coordenada[0] < len(self.mundo[0])
            and nueva_coordenada[1] >= 0 and nueva_coordenada[1] < len(self.mundo) 
            and (self.mundo_aux[nueva_coordenada[0]][nueva_coordenada[1]] != 8 and self.mundo_aux[nueva_coordenada[0]][nueva_coordenada[1]] != 9)):
            return True
        else: return False


    def nuevas_direcciones(self) -> None:
        self.direcciones = {
            "A": (self.coordenadas[0]-1, self.coordenadas[1]+2),
            "B": (self.coordenadas[0]-2, self.coordenadas[1]+1),
            "C": (self.coordenadas[0]-2, self.coordenadas[1]-1),
            "D": (self.coordenadas[0]-1, self.coordenadas[1]-2),
            "E": (self.coordenadas[0]+1, self.coordenadas[1]-2),
            "F": (self.coordenadas[0]+2, self.coordenadas[1]-1),
            "G": (self.coordenadas[0]+2, self.coordenadas[1]+1),
            "H": (self.coordenadas[0]+1, self.coordenadas[1]+2),
        }


'''
        if self.verifica_movimiento(self.direcciones["A"]):
            new_nodo = Nodo(self.mundo, self.direcciones["A"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["B"]):
            new_nodo = Nodo(self.mundo, self.direcciones["B"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["C"]):
            new_nodo = Nodo(self.mundo, self.direcciones["C"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["D"]):
            new_nodo = Nodo(self.mundo, self.direcciones["D"], 4)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["E"]):
            new_nodo = Nodo(self.mundo, self.direcciones["E"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["F"]):
            new_nodo = Nodo(self.mundo, self.direcciones["F"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["G"]):
            new_nodo = Nodo(self.mundo, self.direcciones["G"], 3)
            lista_movimientos.append(new_nodo)
        if self.verifica_movimiento(self.direcciones["H"]):
            new_nodo = Nodo(self.mundo, self.direcciones["H"], 3)
            lista_movimientos.append(new_nodo)
'''