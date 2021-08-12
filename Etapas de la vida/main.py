#Ingrese su edad y muestre la informacion segui la edad
edad = int(input('Ingresa tu edad: '))

if edad >=0 and edad <= 10:
    print('Disfruta tu infancia.')
elif edad >= 11 and edad <= 20:
    print('Muchos cambios y muchos estudios.')
elif edad >= 21 and edad <= 30:
    print('Mucho amor y mucho trabajo')
else:
    print('Opcion fuera del rango')

