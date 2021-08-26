# Función con argumentos variables para sumar todos los valores recibidos

def sumar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado
    

print(sumar(1,1,1,1,1,1,1,1,1,1))