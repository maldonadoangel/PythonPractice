class Persona():
    def __init__(self, nombre =  'Nombre no definido', apellido = 'Apellido no definido', edad = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona()
print(persona1.nombre)
print('------------------')
print()
persona2 = Persona('Angel Hernan', 'Morales Maldonado', 23)
print(persona2.nombre)
print(persona2.apellido)
#Imprimimos la edad a traves de los parametros y el fstring
print(f'Tu edad es de {persona2.edad} años')
print()
print('Modificamos la persona 2')
#Modificamos los atributos de nuestras clases
persona2.nombre = 'Jason'
persona2.apellido = 'Mencoz'
persona2.edad = 30
print(persona2.nombre)
print(persona2.apellido)
print(f'Tu edad es de {persona2.edad} años')
print()

#Tercer objeto creado en una sola linea de texto
persona3 = Persona('Juan', 'Castillo', 26)
print(f'Tu nombre es: {persona3.nombre}, tu apellido es: {persona3.apellido} y tu edad es de {persona3.edad} años')