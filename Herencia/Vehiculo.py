class Vehiculo():
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    @property
    def ruedas(self):
        return self._ruedas
    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas
    
    def __str__(self):
        return f'color: {self._color}, cantidad de ruedas: {self._ruedas}'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad = '0 KM/hr'):
        super().__init__(color, ruedas)
        self._velocidad = velocidad
        
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    def __str__(self):
        return f'Coche: {super().__str__()}, {self._velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo = 'Urbana/Montaña/etc'):
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo
    
    def __str__(self):
        return f'Bicicleta: {super().__str__()}, {self._tipo}'
    
        
if __name__ == '__main__':
    vehiculo = Vehiculo('Rojo', 4)
    print(vehiculo)
    bici = Bicicleta('Azul', 2, 'Urbana')
    print(bici)
    coche = Coche('Negro', 4, '200 KM/hr')
    print(coche)

#
print(__name__)