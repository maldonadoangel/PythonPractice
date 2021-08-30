class Persona():
    def __init__(self, nombre = 'Indefinido', apellido = 'Apellido indefinido', edad = 0, dpi = 'Sin dpi'):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dpi = dpi
    def mostrarDetalle(self):
        print(f'Persona: nombre: {self.nombre}, apellidos: {self.apellido}, edad: {self.edad}, dpi: {self.dpi}')

persona1 = Persona('Yessica Leticia', 'Baten Lopez', 25, '546822120106')
persona1.mostrarDetalle()
#Agregamos un nuevo atributo a nuestra persona1, solo puede acceder persona1 a este atributo a nuestra persona1
persona1.telefono = '500088915'
print(f'Telefono: {persona1.telefono}')

#Este metodo no es comun pero es otra forma de llamar nuestro objeto atraves de nuestra clase principal
# Persona.mostrarDetalle(persona1)        
