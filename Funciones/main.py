
#parametros se pasan en el () de nuestra funcion a traves de los argumentos
def mi_funcion(nombre, apellido):
    print(f'Hola {nombre} {apellido}, estoy Saludando desde mi funcion')


#los argumentos son los valores que pasamos nosotros
mi_funcion('Angel', 'Morales')

mi_funcion('Karla', 'Lara')
#Solicitando valores como argumentos para pasarlo como paramentros en la funcion
name = input('Ingresa tu nombre: ')
last_name = input('Ingresa tu apellido: ')

resultado = mi_funcion(name, last_name)

print(resultado)