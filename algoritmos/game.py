from horse import Horse

test_list = [ # maquina -> 9, humano -> 8
    [9, 0, 0, 3, 0],
    [1, 0, 3, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 5, 0, 8, 0],
    [1, 0, 0, 0, 0],
]
profundidad = 2

horse1 = Horse(test_list, (0, 0), (3, 3), 9, 0)
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




for a in horse1.nuevos_movimientos:
    print(len(a))
    print(a[0].mundo)
    #print(a[1].coordenadas)

print(a[0].padre.mundo)

#horse1 = Horse(test_list, (4, 4), 1, 0, 2)
#horse1.movimientos()