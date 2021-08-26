# Función con argumentos variables para multiplicar los valores

def multiplicar(*numeros):
    total = 1
    for numero in numeros:
        total *= numero
    return total

print(multiplicar(1,2,3,4))