class AreaRectangulo():
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura
    def areaRectangulo(self):
        return self.base * self.altura

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: ")) 
    
area = AreaRectangulo(base, altura)

print(f'El area de tu rectangulo es: {area.areaRectangulo()}')
        