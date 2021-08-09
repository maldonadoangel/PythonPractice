#Solicite al usuario que ingrese la informacion de el libro, imprima todos los datos registrados al final

nombre = input('Ingrese el nombre del libro: ')
numeroIdentificacion = int(input('Ingrese el id del libro: '))
precio = float(input('Ingrese el precio del libro: '))
envio = input('El envio es Gratuito? (True/False): ')
print()

print(f'El nombre del libro es: {nombre}')
print(f'El numero de id: {numeroIdentificacion}')
print(f'El precio del libro es: {precio}')
print(f'Tiene envio gratis? {envio}')
