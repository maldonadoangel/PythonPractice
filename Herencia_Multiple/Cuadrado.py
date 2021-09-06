from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #NORMALMENTE SE USA SUPER PARA LLAMAR LA CLASE PADRE, PERO AQUI TENEMOS HERENCIA MULTIPLES
        #CUAL MANDARIA A LLAMAR?, BUENO AHORA UTILIZAMOS ESTA SINTAXIS
        #super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def calcularArea(self):
        return self._alto * self._ancho
    