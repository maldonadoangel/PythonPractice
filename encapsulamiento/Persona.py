class Persona():
    def __init__(self, nombre, apellido, edad, telefono):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._telefono = telefono
    
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
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono 
        
    def mostrarPersona(self):
        print(f'Tu nombre es: {self._nombre} y tu apellido es: {self._apellido}, tienes {self._edad} años y tu numero de celular es el {self._telefono}')
        

