#diccionario esta compuesto por (key, value)
diccionario = {
    'IDE': 'Integrated Develoment Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)
print(len(diccionario))

for i in diccionario:
    print(diccionario[i])

print()
#Modificar elementos del diccionario
diccionario['OOP'] = 'Modifique el texto'
print(diccionario)
print()
#Accediendo a las llaves y values
for key, value in diccionario.items():
    print(key, value)
    

print()
#recuperando las llaves
for key in diccionario.keys():
    print(key)
print()
#recuperando solo los valores
for value in diccionario.values():
    print(value)

print()

#comprobar si existe un elemento en el diccionario
print('IDE' in diccionario)
#Agregar elementos a nuestra llave primaria
diccionario['PK'] = 'Primary key'
print(diccionario)
#remover elemento de nuestro diccionario
diccionario.pop('IDE')
print(diccionario)
#limipar diccionario
diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario
print(diccionario)