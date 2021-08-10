#Escoger numeros del 1 al 3 para convertir los numeros enteros en texto
numero = int(input('Ingrese un valor del 1 al 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero uno'
 
elif numero == 2:
    numeroTexto = 'Numero Dos'
  
elif numero == 3:
    numeroTexto = 'Numero Tres'
   
else:
    print('Numero invalido')

print(f'Numero proporcionado: {numero}: {numeroTexto}')