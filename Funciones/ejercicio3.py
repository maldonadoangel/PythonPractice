#Crear una funcion recursiva que imprima los numeros del 5 al 1

def descendente(numero):
    if numero == 0:
        return 0
    else:
        while numero != 0:
            print(numero)
            total = descendente(numero-1)
            return total

descendente(5)
print()
descendente(10)