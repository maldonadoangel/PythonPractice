frutas = ['Manzana', 'Pera', 'Platano', 'Uva']
listaVacia = []

print(frutas)
print(len(frutas))

for i in frutas:
    if i == 'Manzana':
        listaVacia.append(i)
        print(f'Encontramos la fruta buscada: {listaVacia}')
else:
    print('Fin del ciclo')