from Cuadrado import Cuadrado
cuadrado1 = Cuadrado(4, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())

#MRO - Method Resolution Order, Imprimimos el orden en como se ejecuta el codigo, debido a la complejidad de la herencia multiples
#Nos muestra una mejor vision de lo que desarollamos
print(Cuadrado.mro())