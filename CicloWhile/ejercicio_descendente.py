#Imprimir los numeros del 5 al 0

numero = int(input('Ingrese un numero entero: '))

while numero > 0:
    print(f'TU numero vale: {numero}')
    numero -= 1
else:
    print('Fin del ciclo')