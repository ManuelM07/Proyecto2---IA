""" 
Archivo encargado de manejar las entradas del usuario y mostrar
en pantalla el objeto de estado actual del juego (GameState).
"""
import pygame as pg
from ChessEngine import EstadoJuego
ANCHO = 512 #400
ALTO = ANCHO
DIMENSION = 8 #dimensiones de un tablero de ajedrez 8x8
TAM_CUADRADO = ALTO // DIMENSION
MAX_FPS = 15 #para las animaciones
IMAGENES = {}

""" 
Inicializar un diccionario global de imágenes. Se llamará solo una vez desde el main.
"""
def cargar_imagenes():
    piezas = ['bN', 'wN', "ce", "fl", "ma"]
    for pieza in piezas:
        IMAGENES[pieza] = pg.transform.scale(pg.image.load("resources/" + pieza + ".png"), (TAM_CUADRADO, TAM_CUADRADO))

""" 
Principal driver del código, Manejará la entrada del usuario y actualizará los gráficos.
"""
def main():
    pg.init()
    pantalla = pg.display.set_mode((ANCHO, ALTO))
    clock = pg.time.Clock()
    pantalla.fill(pg.Color("white"))
    estado_juego = EstadoJuego()
    cargar_imagenes()
    ejecutando = True
    while ejecutando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                ejecutando = False
        dibujarEstadoJuego(pantalla, estado_juego)
        clock.tick(MAX_FPS)
        pg.display.flip()

def dibujarEstadoJuego(pantalla, estado_juego):
    dibujarTablero(pantalla)
    dibujarPiezas(pantalla, estado_juego.tablero)


def dibujarTablero(pantalla):
    colores = [pg.Color(232,188,144), pg.Color(202,137,61)]
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            color = colores[((fila+columna) % 2)]
            pg.draw.rect(pantalla, color, pg.Rect(columna*TAM_CUADRADO, fila*TAM_CUADRADO, TAM_CUADRADO, TAM_CUADRADO))

def dibujarPiezas(pantalla, tablero):
    pass

if __name__ == "__main__":
    main()