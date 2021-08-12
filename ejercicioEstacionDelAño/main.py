mes = int(input('Ingrese el mes del año 1-12'))
temporada = ''

if mes == 1 or mes == 2 or mes == 12:
    temporada = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    temporada = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    temporada = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    temporada = 'Otoño'
else:
    print('Mes erroneo')

print(f'El mes que ingresaste: {mes}: {temporada}')