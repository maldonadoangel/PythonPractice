class Persona():
    def __init__(self, nombre, apellido, edad, telefono):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono

    def mostrarPersona(self):
        print(f'Tu nombre es: {self._nombre} y tu apellido es: {self.apellido}, tienes {self.edad} años y tu numero de celular es el {self.telefono}')
        
persona = Persona('Angel Hernan', 'Morales Maldonado', 23, '50088915')
#Modificamos el atributo encapsulado
persona._nombre = 'Hernan Jose'
persona.mostrarPersona()
persona.dpi = '2988166440101'
print(persona.dpi)
        