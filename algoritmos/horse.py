
# caballo1 -> 1 -> machine
# caballo2 -> 2 -> humanoide

class Horse:

    def __init__(self, mundo, coordenadas, tipo_jugador, total_puntos) -> None:
        self.mundo = mundo
        self.tipo_jugador = tipo_jugador
        self.total_puntos = total_puntos
        self.coordenadas = coordenadas # coordenadas del caballo
        self.nuevos_movimientos = []

# [nodo1, nodo2, nodo3, nodo4]
# [ [ [nodo1, nodo2, nodo3], nodo2, nodo3, nodo4] ]
    
    def movimientos(self) -> None:
        if self.verifica_movimiento((self.coordenadas[0]-1, self.coordenadas[1]+2)):
            print(1)
        if self.verifica_movimiento((self.coordenadas[0]-2, self.coordenadas[1]+1)):
            print(2)
        if self.verifica_movimiento((self.coordenadas[0]-2, self.coordenadas[1]-1)):
            print(3)
        if self.verifica_movimiento((self.coordenadas[0]-1, self.coordenadas[1]-2)):
            print(4)
        if self.verifica_movimiento((self.coordenadas[0]+1, self.coordenadas[1]-2)):
            print(5)
        if self.verifica_movimiento((self.coordenadas[0]+2, self.coordenadas[1]-1)):
            print(6)
        if self.verifica_movimiento((self.coordenadas[0]+2, self.coordenadas[1]+1)):
            print(7)
        if self.verifica_movimiento((self.coordenadas[0]+1, self.coordenadas[1]+2)):
            print(8)
        


    def verifica_movimiento(self, nueva_coordenada):
        if (nueva_coordenada[0] >= 0 and nueva_coordenada[0] < len(self.mundo[0])
            and nueva_coordenada[1] >= 0 and nueva_coordenada[1] < len(self.mundo) 
            and self.mundo[nueva_coordenada[0]][nueva_coordenada[1]] != 2):
            return True
        else: return False
