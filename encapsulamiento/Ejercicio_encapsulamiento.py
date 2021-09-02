class Alumno():
    def __init_(self, nombre = 'No definido', apellido = 'No definido', grado = 'No definido', carnet = 'No definido'):
        self._nombre = nombre
        self._apellido = apellido
        self._grado = grado
        self._carnet = carnet
    #metodo get
    @property
    def nombre(self):
        return self._nombre
    
    #metodo set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

alumno = Alumno()
alumno.nombre = input("Ingresa tu nombre: ")
alumno.apellido = input('Ingresa tu apellido: ')
alumno.grado = input('Ingresa tu grado: ')
alumno.carnet = input('Ingresa tu carnet: ')

print(f'Bienvenido {alumno.nombre} {alumno.apellido}, tu grado es: {alumno.grado} y tu numero de carnet es: {alumno.carnet}')