class Persona():
    def __init__(self, nombre =  'Nombre no definido', apellido = 'Apellido no definido', edad = 0, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        
    
#Creamos metodos para nuestra clase persona
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')
        

#Utilizamos el metodo de mostrar detalle para persona1
persona1 = Persona('Yessica', 'Lopez', 25, '123123', 12,23,123,32, comidaFavorita='Pizza', marcaCelular='Samsung')
print(persona1.mostrarDetalle())
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