class Nodo:

    def __init__(self,  mundo, coordenadas, utilidad, padre) -> None:
        self.mundo = mundo
        self.coordenadas = coordenadas
        self.utilidad = utilidad
        self.padre = padre


    #def __eq__(self, __o: object) -> bool:
    #    return self.utilidad > __o.utilidad


    #def __lt__(self, other):
    #    return self.utilidad > other.utilidad