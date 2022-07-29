from horse import Horse

test_list = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
profundidad = 2

horse1 = Horse(test_list, (4, 4), 1, 0, 2)
for i in range(profundidad):
    if i:
        for j in range(len(horse1.nuevos_movimientos)):
            #print(horse1.nuevos_movimientos)
            #print(j)
            horse1.coordenadas = horse1.nuevos_movimientos[j].coordenadas
            horse1.nuevos_movimientos[j] = horse1.movimientos()
    else: 
        horse1.nuevos_movimientos = horse1.movimientos()



for a in horse1.nuevos_movimientos:
    print(len(a))
    print(a)
    print(a[0].coordenadas)

#horse1 = Horse(test_list, (4, 4), 1, 0, 2)
#horse1.movimientos()