from horse import Horse
from padre_hijo import PadreHijo
from profundidad import Profundidad
import numpy as np
import queue


all_profundidad = []
test_list = [ # maquina -> 9, humano -> 8
    [9, 0, 0, 3, 0],
    [1, 0, 3, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 5, 0, 8, 0],
    [1, 0, 0, 0, 0],
]
profundidad = 6

horse1 = Horse(test_list, (0, 0), (3, 3), 9, 0)
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
        print(f"longitud: {(all_profundidad[i-1].total_nodos())}")
        j = 0
        for _ in range(all_profundidad[i-1].total_nodos()): # itera la cantidadad de nodos que se generaron en la anterior profundidad
            print("problem",all_profundidad[i-1].padres_hijos[count])
            #exit()
            try:
                horse1.padre = all_profundidad[i-1].padres_hijos[count].hijos[j] #horse1.nuevos_movimientos[j]
            except IndexError:
                try: # TODO esta excepción se debería quitar, pero verificar antes
                    j = 0
                    count += 1
                    print("problemx",all_profundidad[i-1].padres_hijos[count].hijos)
                    horse1.padre = all_profundidad[i-1].padres_hijos[count].hijos[j] #horse1.nuevos_movimientos[j]
                #horse1.nuevos_movimientos[j] = horse1.movimientos()
                except IndexError:
                    count += 1
            j += 1
            hijos = horse1.movimientos().copy()

            aux_profundidad = np.append(aux_profundidad.copy(), PadreHijo(horse1.padre, hijos.copy()))

        
        ###########
    else: 
        #horse1.posibles_movimientos = horse1.movimientos()
        hijos = horse1.movimientos()
        horse1.nuevos_movimientos = hijos.copy()
        aux_profundidad = np.append(aux_profundidad, PadreHijo(hijos=hijos.copy()))
        print(hijos)
        print(f"Primero: {horse1.nuevos_movimientos[1]}")
    all_profundidad.append(Profundidad(aux_profundidad.copy()))



'''for a in horse1.nuevos_movimientos:
    print(len(a))
    print(a[0].mundo)
    #print(a[1].coordenadas)

print(a[0].padre.mundo, a[0].padre.coordenadas)'''


def _max(lista):
    o_max = (lista[0], lista[0].utilidad)
    for i in range(1, len(lista)):
        if lista[i].utilidad >= o_max[1]:
            o_max = (lista[i], lista[i].utilidad)
    return o_max[0]
        

def _min(lista):
    o_min = (lista[0], lista[0].utilidad)
    for i in range(1, len(lista)):
        if lista[i].utilidad <= o_min[1]:
            o_min = (lista[i], lista[i].utilidad)
    return o_min[0]


def obtener_movimiento():
    lista_movimientos = horse1.nuevos_movimientos.copy()
    lista_aux = []
    for i in range(profundidad):
        if i%2==0:
            for obj in lista_movimientos:
                lista_aux.append(_min(obj))
        else:
            for obj in lista_movimientos:
                lista_aux.append(_max(obj))
        lista_movimientos = [lista_aux.copy()]
        lista_aux = []
    return lista_movimientos[0]

#x = obtener_movimiento()
#print(x[0].padre.coordenadas)
print(_min(all_profundidad[5].padres_hijos[0].hijos).utilidad)
#print(horse1.nuevos_movimientos)

'''            def recursive_list(lista=None, obj=None):
                horse1.padre = horse1.nuevos_movimientos[j]
                horse1.nuevos_movimientos[j] = horse1.movimientos()
                if obj == []:
                    if type(lista) == list:
                        if lista == []:
                            return []
                        else:
                            return recursive_list(lista[1:], lista[0])
                    else:
                        return recursive_list(obj=lista[0])
                else: 
                    pass'''

'''
La que funciona:

#horse1.nuevos_movimientos
for i in range(profundidad):
    if i:
        if horse1.tipo_jugador == 9:
            horse1.tipo_jugador = 8
            horse1.coordenadas = horse1.coordenadas_humano
        else:
            horse1.tipo_jugador = 9
            horse1.coordenadas = horse1.coordenadas_maquina

        for j in range(len(horse1.nuevos_movimientos)):
            #print(horse1.nuevos_movimientos)
            #print(j)
            #horse1.coordenadas = horse1.nuevos_movimientos[j].coordenadas
            horse1.padre = horse1.nuevos_movimientos[j]
            horse1.nuevos_movimientos[j] = horse1.movimientos()
    else: 
        #horse1.posibles_movimientos = horse1.movimientos()
        horse1.nuevos_movimientos = horse1.movimientos()
        print(f"Primero: {horse1.nuevos_movimientos[1]}")
'''