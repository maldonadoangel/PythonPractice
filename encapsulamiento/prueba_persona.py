from Persona import Persona


print('Creacion de objetos'.center(100,'-'))
persona1 = Persona("Angel Hernán", "Morales Maldonado", 23, '50088915')
persona1.mostrarPersona()
print('Eliminacion de caracteres'.center(100,'-'))
#Eliminamos el objeto persona 1 y si intentamos llamarlo, nos mostrara un error de persona1 is not defined
del persona1
persona1.mostrarPersona()

print()
print('Objeto 2 creado'.center(100,'-'))
#Creamos otro objeto de la clase Persona 
persona2 = Persona('Rick', 'Sanchez', 63, '0000000')
persona2.mostrarPersona()

