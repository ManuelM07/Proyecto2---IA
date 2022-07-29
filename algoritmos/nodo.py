class Nodo:

    def __init__(self,  mundo, coordenadas, utilidad, padre) -> None:
        self.mundo = mundo
        self.coordenadas = coordenadas
        self.utilidad = utilidad
        self.padre = padre
