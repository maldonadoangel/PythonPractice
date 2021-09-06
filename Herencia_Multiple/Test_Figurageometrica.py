from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(4, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())

#MRO - Method Resolution Order, Imprimimos el orden en como se ejecuta el codigo, debido a la complejidad de la herencia multiples
#Nos muestra una mejor vision de lo que desarollamos
print(Cuadrado.mro())

rectangulo = Rectangulo(5, 5, 'Verde')
print(rectangulo.alto)
print(rectangulo.ancho)
print(f'Calcular el area del rectangulo es: {rectangulo.calcular_area()}, con un color: {rectangulo.color}')