operadorA = 4
operadorB = 4

suma = operadorA + operadorB
#print(suma)
print(f'El resultado suma: {suma}')

#Resta

resta = operadorA - operadorB
print(f'El resultado de la resta: {resta}')

#Multiplicacion
multiplicacion = operadorA * operadorB
print(f'El resultado de multiplicar: {multiplicacion}')

#division
if operadorB == 0:
    division = operadorB / operadorA
    print(f'El resultado de la division es: {division}')
elif operadorA >= operadorB:
    division = operadorA / operadorB
    print(f'El resultado de la division es: {division}')
    
    