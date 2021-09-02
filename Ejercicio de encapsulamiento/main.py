#Crear una calculadora, utilizando el concepto de clases, objetos y encapsulamiento del
class Calculadora():
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    
    @property
    def suma(self):
        return self._numero1 + self._numero2
    @suma.setter
    def suma(self, numero1, numero2):
        self._numero1 = numero1 
        self._numero2 = numero2
    @property
    def resta(self):
        return self._numero1 - self._numero2
    @resta.setter
    def resta(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    @property
    def multiplicacion(self):
        return self._numero1 * self._numero2
    @multiplicacion.setter
    def multiplicacion(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2
    @property
    def division(self):
        return self._numero1 / self._numero2
    @division.setter
    def division(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2

print('Bienvenido a mi calculadora')
print('Menu de opciones: ')
print('1. Suma')
print('2. Resta')
print('3. multiplicacion')
print('4.division')
print('5. salir')
opcion = int(input('Ingrese una opcion: '))

if opcion == 1:
    print('Bienvenido a la opcion de suma')
    num1 = float(input("Ingrese su primer valor: "))
    num2 = float(input('Ingrese su segundo valor: '))
    sumar = Calculadora(num1, num2)
    print(f'El resultado total de la suma es: {sumar.suma} ')
elif opcion == 2:
    print('Bienvenido a la opcion de resta')
    num1 = float(input('Ingresa tu primer valor: '))
    num2 = float(input('Ingresa tu segundo valor: '))
    restar = Calculadora(num1, num2)
    print(f'El resultado total de la resta es: {restar.resta}')
elif opcion == 3:
    print('Bienvenido a la opcion de multiplicacion')
    num1 = float(input('Ingresa tu primer valor: '))
    num2 = float(input('Ingresa tu segundo valor: '))
    multiplo = Calculadora(num1, num2)
    print(f'El resultado total de la multiplicacion es: {multiplo.multiplicacion}')
elif opcion == 4:
    print('Bienvenido a la opcion de division')
    num1 = float(input('Ingresa tu primer valor:'))
    num2 = float(input('Ingresa tu segundo valor: '))
    if num2 == 0:
        print('Error no puede ingresar el valor de cero en el denominador, se sumara un 1 al valor ingresado.')
        num2 += 1
    div = Calculadora(num1, num2)
    print(f'El resultado de la division es: {div.division}') 
elif opcion == 5:
    print('Saliendo del programa.....')
    exit()
else:
    print('Ingreso una opcion incorrecta')