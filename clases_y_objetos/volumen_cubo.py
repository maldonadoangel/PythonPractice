class VolumenCubo():
    def __init__(self, ancho = 0, alto = 0, profundo = 0):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input('Ingrese el ancho de su cubo: '))
alto = int(input('Ingrese el alto de su cubo: '))
profundo = int(input('Ingrese la profundidad de su cubo: '))

cubo = VolumenCubo(ancho, alto, profundo)
print(f'El volumen de su cubo es: {cubo.calcularVolumen()}')
        