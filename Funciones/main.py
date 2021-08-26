def sumar(a,b):
    return a+b

total = sumar(5,5)

print(f'La suma de nuestra funcion es: {total}')    



#Parametros por defecto, nos ayuda a no dejar sin rellenar algun parametro
def resta(a = 0, b = 0):
    return a-b



sustraccion = resta()
print(f'La resta de la funcion es: {sustraccion}')
print()

#parametros variables en una funcion, cuando desconocemos la cantidad de parametros que van a ingresar
def lista_nombres(*nombres):
    for nombre in nombres:
        print(f'nombre: {nombre}    ')

lista = lista_nombres('Angel', 'Hernan', 'Jose', 'Herni')

print(lista)

#Argumentos llave valor
def listarTerminos(**kwargs):
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listarTerminos(KEY='llave', POO = 'Progamacion orientada en objetos')