#SET en python, no mantienen orden o indice, no se pueden modificar los elementos que especifiquemos
#pero podemos agregar nuevos elementos

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
#conocer el largo 
print(len(planetas))
# revisar si un elemento esta presente, tambien se puede realizar en listas o tuplas
print('Marte' in planetas)
#agregar elementos
planetas.add('Tierra')
print(planetas)