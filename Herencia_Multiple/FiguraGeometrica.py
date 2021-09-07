#ABC ABSTRACT BASE CLASS
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto
        #Propiedades getter and setter
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto
#Clases abstractas, nos obliga a colocar una funcion especifica por la clase padre hacia las clases hijas
    @abstractmethod
    def calcularArea(self):
        pass
    
    def __str__(self):
        return f'Figura Geometrica: {self._ancho} {self._alto}'

