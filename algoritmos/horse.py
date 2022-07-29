from numpy import append
from nodo import Nodo

# caballo1 -> 1 -> machine
# caballo2 -> 2 -> humanoide
DIRECCIONES = ["A", "B", "C", "D", "E", "F", "G", "H"]

class Horse:

    def __init__(self, mundo, coordenadas, tipo_jugador, total_puntos, profundidad) -> None:
        self.mundo = mundo
        self.tipo_jugador = tipo_jugador
        self.total_puntos = total_puntos
        self.coordenadas = coordenadas # coordenadas del caballo
        self.nuevos_movimientos = []
        self.direcciones = {}

# [nodo1, nodo2, nodo3, nodo4]
# [ [ [nodo1, nodo2, nodo3], nodo2, nodo3, nodo4] ]
    
    def movimientos(self) -> list:
        self.nuevas_direcciones()
        lista_movimientos = []

        for i in range(8):
            if self.verifica_movimiento(self.direcciones[DIRECCIONES[i]]):
                new_nodo = Nodo(self.mundo, self.direcciones[DIRECCIONES[i]], 3)
                lista_movimientos.append(new_nodo)
        
        return lista_movimientos
        


    def verifica_movimiento(self, nueva_coordenada) -> bool:
        if (nueva_coordenada[0] >= 0 and nueva_coordenada[0] < len(self.mundo[0])
            and nueva_coordenada[1] >= 0 and nueva_coordenada[1] < len(self.mundo) 
            and self.mundo[nueva_coordenada[0]][nueva_coordenada[1]] != 2):
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