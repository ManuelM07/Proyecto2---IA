""" 
Archivo encargado de manejar las entradas del usuario y mostrar
en pantalla el objeto de estado actual del juego (GameState).
"""
import pygame as pg
import ChessEngine 
ANCHO = 512  #400
ALTO = ANCHO 
DIMENSION = 8 #dimensiones de un tablero de ajedrez 8x8
TAM_CUADRADO = ALTO // DIMENSION
MAX_FPS = 15 #para las animaciones
IMAGENES = {}

puntaje_ia = 0
puntaje_jugador = 0
marcador = [puntaje_ia, puntaje_jugador]

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
    pg.display.set_caption('Hungry Horses 1.0')
    pg.display.set_icon(pg.image.load("resources/images/wN.png"))
    clock = pg.time.Clock()
    pantalla.fill(pg.Color("white"))
    estado_juego = ChessEngine.EstadoJuego()
    movimientos_val = estado_juego.get_mov_validos()
    print("mov válidos: ", movimientos_val)
    movimiento_hecho = False # variable bandera para cuando se realiza un movimiento


    cargar_imagenes()
    ejecutando = True
    cuadrado_seleccionado = () #no hay cuadrado seleccionado, guarda (fila, columna)
    clicks_jugador = [] #guarda los clicks del jugador -> (dos tuplas: [(fil1, col1), (fil2, col2)])
    while ejecutando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                ejecutando = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                localizacion = pg.mouse.get_pos() #pos x,y del ratón
                columna = localizacion[0] // TAM_CUADRADO
                fila = localizacion[1] // TAM_CUADRADO
                if cuadrado_seleccionado == (fila, columna): #el usuario seleccionó el mismo cuadrado
                    cuadrado_seleccionado = () #eliminar la selección anterior, "deseleccionar"
                    clicks_jugador = []
                else:
                    cuadrado_seleccionado = (fila, columna)
                    clicks_jugador.append(cuadrado_seleccionado)
                if len(clicks_jugador) == 2:
                    mover = ChessEngine.Mover(clicks_jugador[0], clicks_jugador[1], estado_juego.tablero)
                    print(mover.getNotacionAjedrez())
                    
                    if mover in movimientos_val:
                        estado_juego.realizar_movimiento(mover)
                        #print("pieza capturada: ", mover.pieza_capturada)
                        movimiento_hecho = True
                        cuadrado_seleccionado = () #restablecer los clicks del usuario
                        clicks_jugador = []
                        print("marcador: ", estado_juego.marcador)
                    else: 
                        print("¡movimiento inválido!")
                        clicks_jugador = [cuadrado_seleccionado]
                    


        if movimiento_hecho:
            movimientos_val = estado_juego.get_mov_validos()
            movimiento_hecho = False

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
    for fila in range(DIMENSION):
        for columna in range(DIMENSION):
            pieza = tablero[fila][columna]
            if pieza != "--": #una pieza no vacía
                pantalla.blit(IMAGENES[pieza], pg.Rect(columna*TAM_CUADRADO, fila*TAM_CUADRADO, TAM_CUADRADO, TAM_CUADRADO))

if __name__ == "__main__":
    main()