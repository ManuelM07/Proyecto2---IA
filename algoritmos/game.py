from horse import Horse
from padre_hijo import PadreHijo
from profundidad import Profundidad
import numpy as np


all_profundidad = []
test_list = [ # maquina -> 9, humano -> 8
    [9, 1, 0, 3, 0], # 0
    [1, 0, 8, 0, 1], # 1
    [0, 1, 0, 5, 1], # 2
    [3, 5, 0, 0, 0], # 3
    [1, 0, 0, 0, 0], # 4
]
profundidad = 6

mundo_aux = [ # maquina -> 9, humano -> 8
    [0, 1, 0, 3, 0, 3, 0, 0], # 0
    [0, 1, 1, 3, 5, 0, 0, 0], # 1
    [0, 1, 9, 3, 0, 1, 0, 0], # 2
    [0, 1, 1, 8, 1, 0, 3, 0], # 3
    [0, 1, 0, 3, 0, 5, 0, 0], # 4
    [0, 1, 1, 3, 1, 0, 0, 0], # 5
    [0, 1, 0, 3, 0, 3, 0, 0], # 6
    [0, 1, 0, 3, 0, 0, 3, 0], # 7
]
#cantidad_nodos = 0

# machine = 5 5 5 1 3
# humanoide = 3 3 3 1 1 1 1 1

horse1 = Horse(mundo_aux, (2, 2), (3, 3), 9, 0)
#horse1.nuevos_movimientos
for i in range(profundidad): # itera la cantidad de profundidades que hay
    count = 0
    aux_profundidad = np.array([])
    if i: # se verifica quien viene con el turno para pasarselo al otro participante
        if horse1.tipo_jugador == 9:
            horse1.tipo_jugador = 8
            horse1.coordenadas = horse1.coordenadas_humano
        else:
            horse1.tipo_jugador = 9
            horse1.coordenadas = horse1.coordenadas_maquina

        ##########
        #print(f"longitud: {(all_profundidad[i-1].total_nodos())}")
        j = 0
        #cantidad_nodos += all_profundidad[i-1].total_nodos()
        for _ in range(all_profundidad[i-1].total_nodos()): # itera la cantidadad de nodos que se generaron en la anterior profundidad, 
                                                            # ya que esos hijos se convierte en los padres de la profundidad siguiente
        #    print("problem",all_profundidad[i-1].padres_hijos[count])
            #exit()
            try:
                horse1.padre = all_profundidad[i-1].padres_hijos[count].hijos[j] #horse1.nuevos_movimientos[j]
            except IndexError:
                j = 0
                count += 1
                #print("problemx",all_profundidad[i-1].padres_hijos[count].hijos)
                horse1.padre = all_profundidad[i-1].padres_hijos[count].hijos[j] #horse1.nuevos_movimientos[j]

            j += 1
            hijos = horse1.movimientos()

            aux_profundidad = np.append(aux_profundidad, PadreHijo(horse1.padre, hijos))        
        ###########
    else: 
        hijos = horse1.movimientos()
        horse1.nuevos_movimientos = hijos
        aux_profundidad = np.append(aux_profundidad, PadreHijo(hijos=hijos))
    all_profundidad.append(Profundidad(aux_profundidad))


def _max(lista) -> bool:
    """recorre una lista de padre-hijos, determinando 
    cual es el hijo max de cada conjunto de padre-hijos
    guarda la decisión en el atributo nodo_elegido del padre correspondiente"""
    for padre_hijos in lista:
        sub_hijos = padre_hijos.hijos
        o_max = (sub_hijos[0].nodo_elegido, sub_hijos[0].nodo_elegido.utilidad)
        for i in range(1, len(sub_hijos)):
            if sub_hijos[i].nodo_elegido.utilidad > o_max[1]:
                o_max = (sub_hijos[i].nodo_elegido, sub_hijos[i].nodo_elegido.utilidad)        
        try: # En la profundidad 1, los nodos no tienen padres, por consecuencia no tienen nodos elegidos, 
             # por lo anterior se captura la excepción de tipo AttributeError y se crea un nuevo padre para el nodo en consecuencia
            padre_hijos.padre.nodo_elegido = o_max[0]  
        except AttributeError: 
            padre_hijos.padre = o_max[0]   
    return True
        

def _min(lista) -> bool:
    """recorre una lista de padre-hijos, determinando 
        cual es el hijo menor de cada conjunto de padre-hijos
        guarda la decisión en el atributo nodo_elegido del padre correspondiente"""
    for padre_hijos in lista:
        sub_hijos = padre_hijos.hijos
        o_min = (sub_hijos[0].nodo_elegido, sub_hijos[0].nodo_elegido.utilidad)
        for i in range(1, len(padre_hijos.hijos)):
            if sub_hijos[i].nodo_elegido.utilidad < o_min[1]:
                o_min = (sub_hijos[i].nodo_elegido, sub_hijos[i].nodo_elegido.utilidad)
        padre_hijos.padre.nodo_elegido = o_min[0]        
    return True


def _min_aux(lista) -> bool:
    """Es una extensión de _min(), en esta función no se
        tiene en cuenta el atributo nodo_elegido"""
    for padre_hijos in lista:
        sub_hijos = padre_hijos.hijos
        o_min = (sub_hijos[0], sub_hijos[0].utilidad)
        for i in range(1, len(sub_hijos)):
            if sub_hijos[i].utilidad < o_min[1]:
                o_min = (sub_hijos[i], sub_hijos[i].utilidad)
        padre_hijos.padre.nodo_elegido = o_min[0]
    return True


def obtener_movimiento() -> tuple:
    """Está función se encarga de hacer el recorrido por el arbol,
        aplicando el algoritmo minimax, finalmente retorna la coordenada
        hacia donde debe moverse la maquina"""

    answer = ()
    _min_aux(all_profundidad[profundidad-1].padres_hijos)
    for i in range(profundidad-2, -1, -1):
        if i%2==0:
            _max(all_profundidad[i].padres_hijos)
        else:
            _min(all_profundidad[i].padres_hijos)
        #lista_aux = []
    answer = all_profundidad[0].padres_hijos[0].padre
    for _ in range(profundidad-1): # hace un recorrido hasta el ultimo padre, ya que es el que guarda la coordenada hacia donde debe moverse
        answer = answer.padre
        
    return answer.coordenadas


print((obtener_movimiento()))
#print(all_profundidad[0].padres_hijos[0].padre)
#print(cantidad_nodos)
#print(all_profundidad[profundidad-1].padres_hijos[0].hijos[0].utilidad)