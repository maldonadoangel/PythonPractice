
#Encontrar si esta dentro de la edad de 20 años y 30 años

edad = int(input('Ingrese su edad: '))

if edad >= 20 and edad <= 30:
    print(f'Tu edad se encuentra dentro del rango, ya que tienes {edad} años')
else:
    print(f'Estas fuera de rango, tu edad es: {edad} años')