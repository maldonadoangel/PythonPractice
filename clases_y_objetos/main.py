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
        