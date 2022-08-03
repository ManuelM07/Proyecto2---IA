""" 
Esta clase es responsable de restaurar toda de la información del
estado actual del juego. También será responsable de determinar los
movimientos válidos en el estado actual. También guardará un registro
de movimientos.
"""
class EstadoJuego():
    def __init__(self):
        # el tablero es una lista 8x8 donde cada elemento tiene 2 caracteres
        # -- -> espacio en blanco, wN -> caballo blanco, bN -> caballo negro
        # ce -> césped, fl -> flor, ma -> manzana.
        self.tablero = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
        ]
        self.mueveBlanco = True
        self.registroMovimientos = []