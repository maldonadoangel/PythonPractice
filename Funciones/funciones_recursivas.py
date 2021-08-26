#Crear un programa que calcule el numero factorial, la funcion recursiva es basicamente llamarse a si misma hasta completar lo planeado
#5! -> 5*4*3*2*1 = 120
#4! -> 4*3*2*1 = 24

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
        
        
resultado = factorial(5)
resultado2 = factorial(4)
print(f'EL factorial de 5 es: {resultado}')
print(f'EL factorial de 4 es: {resultado2}')

        