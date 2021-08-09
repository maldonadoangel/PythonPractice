#Encontrar el area y perimetro de un rectangulo

alto = int(input('Ingrese el alto de su rectangulo: '))
ancho = int(input('Ingrese la anchura de su rectangulo: '))
area = alto * ancho
print(f'El area del rectangulo es: {area}')
perimetro = (alto+ancho)*2
print(f'El perimetro del rectangulo es: {perimetro}')
