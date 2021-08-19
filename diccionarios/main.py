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

#Modificar elementos del diccionario
diccionario['OOP'] = 'Modifique el texto'
print(diccionario)