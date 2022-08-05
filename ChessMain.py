""" 
Archivo encargado de manejar las entradas del usuario y mostrar
en pantalla el objeto de estado actual del juego (GameState).
"""
import pygame as pg
import ChessEngine 
from algoritmos.game import  start
from algoritmos.horse import Horse
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
    global movimiento_hecho, pos_actual_wN, clock
    #setup
    pg.init()
    pantalla = pg.display.set_mode((ANCHO, ALTO))
    pg.display.set_caption('Hungry Horses 1.0')
    pg.display.set_icon(pg.image.load("resources/images/wN.png"))
    clock = pg.time.Clock()
    pantalla.fill(pg.Color("white"))

    #variables para el juego.
    estado_juego = ChessEngine.EstadoJuego()
    movimientos_val = estado_juego.get_mov_validos()
    lista_movimientos = list(map(lambda mov: (mov.fila_final, mov.columna_final), movimientos_val))
    print("mov válidos: ", lista_movimientos)
    movimiento_hecho = False # variable bandera para cuando se realiza un movimiento
    horse1 = Horse(estado_juego.nuevo_tablero[0], estado_juego.nuevo_tablero[1], estado_juego.nuevo_tablero[2], 9, 0)
    nueva_coordenada_wN = ()

    cargar_imagenes()
    ejecutando = True
    cuadrado_seleccionado = () #no hay cuadrado seleccionado, guarda (fila, columna)
    clicks_jugador = [] #guarda los clicks del jugador -> (dos tuplas: [(fil1, col1), (fil2, col2)])
    
    #se muestra por primera vez la interfaz gráfica.
    dibujarEstadoJuego(pantalla, estado_juego)
    pg.display.flip()

    pos_actual_wN = ()
    pos_actual_bN = ()
    primerMovimiento(horse1, estado_juego, movimientos_val)
    print("mov_hecho: ", movimiento_hecho)
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
                    lista_movimientos = list(map(lambda mov: (mov.fila_final, mov.columna_final), movimientos_val))
                    print("mov válidos: ", lista_movimientos)
                    print("tablero: ", estado_juego.tablero)
                    print("coordenada:", cuadrado_seleccionado)
                    if mover in movimientos_val:
                        print("el caballo negro se movió")

                        estado_juego.realizar_movimiento(mover)
                        #print("pieza capturada: ", mover.pieza_capturada)
                        movimiento_hecho = True
                        cuadrado_seleccionado = () #restablecer los clicks del usuario
                        clicks_jugador = []
                        pos_actual_bN = (mover.fila_final, mover.columna_final)
                        print("marcador: ", estado_juego.marcador)
                    else: 
                        print("¡movimiento inválido!")
                        clicks_jugador = [cuadrado_seleccionado]
                    
        if estado_juego.mueve_blanco:
            nuevo_tablero = estado_juego.mapear_matriz()
            #horse1 = Horse(estado_juego.nuevo_tablero[0], estado_juego.nuevo_tablero[1], estado_juego.nuevo_tablero[2], 9, 0)
            print("nuevo:", nuevo_tablero[0])
            nueva_coordenada_wN = start(Horse(nuevo_tablero[0], nuevo_tablero[1], nuevo_tablero[2], 9, 0))  

            print("nueva: ", nueva_coordenada_wN) 
            print("válidos: ", (movimientos_val[0].fila_final, movimientos_val[0].columna_final), (movimientos_val[1].fila_final, movimientos_val[1].columna_final))
            mover = ChessEngine.Mover(pos_actual_wN, nueva_coordenada_wN, estado_juego.tablero)
            pos_actual_wN = nueva_coordenada_wN
            #if mover in movimientos_val:
            clock.tick(1)
            estado_juego.realizar_movimiento(mover)
            print("valido caballo blanco")
            movimiento_hecho = True
            print("mov_hecho: ", movimiento_hecho)
            print("marcador: ", estado_juego.marcador)
            cuadrado_seleccionado = () #restablecer los clicks del usuario
            clicks_jugador = []
            #else:
            #    print("¡inválido!")


        if movimiento_hecho:
            print("entra a movimiento_hecho")
            movimientos_val = estado_juego.get_mov_validos()
            movimiento_hecho = False

        dibujarEstadoJuego(pantalla, estado_juego)
        clock.tick(MAX_FPS)
        pg.display.flip()

def primerMovimiento(horse1, estado_juego,  movimientos_val):
    global movimiento_hecho, pos_actual_wN, clock
    nueva_coordenada_wN = start(horse1)   
    pos_actual_wN = nueva_coordenada_wN
    print("nueva: ", nueva_coordenada_wN) 
    print("validos: ", movimientos_val)
    mover = ChessEngine.Mover(estado_juego.nuevo_tablero[1], nueva_coordenada_wN, estado_juego.tablero)
    
    if mover in movimientos_val:
        print("es válido")
        clock.tick(1)
        estado_juego.realizar_movimiento(mover)
        movimiento_hecho = True
        print("marcador: ", estado_juego.marcador)

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