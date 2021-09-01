class Persona():
    def __init__(self, nombre, apellido, edad, telefono):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
    
    #Decorador, modifica el comportamiento de nuestro metodo
    #Esta es la forma de nombrar el metodo getter
    @property
    def nombre(self):
        print('Llamando metodo get nombre')
        return self._nombre
    #esta es la forma de nombrar el metodo setter
    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo set nombre')
        self._nombre = nombre
        
    def mostrarPersona(self):
        print(f'Tu nombre es: {self._nombre} y tu apellido es: {self.apellido}, tienes {self.edad} años y tu numero de celular es el {self.telefono}')
        
persona = Persona('Angel Hernan', 'Morales Maldonado', 23, '50088915')
#Gracias al decorador ya no es necesario colocar parentesis en nombre
#debido a que cambia su comportamiento y es similar al llamar un atributo
print(persona.nombre)
persona.nombre = "Juancho"
print(persona.nombre)