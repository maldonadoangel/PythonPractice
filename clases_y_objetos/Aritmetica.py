class Aritmetica():
    def __init__(self, numero1 = 0.0, numero2 = 0.0, total = 0.0):
        self.numero1 = numero1
        self.numero2 = numero2
        self.total = total
    def suma(self):
        self.total = self.numero1 + self.numero2
        print(f'La suma de {self.numero1} + {self.numero2} = {self.total}')
    def resta(self):
        self.total = self.numero1 - self.numero2
        print(f'La resta de {self.numero1} - self.numero2 = {self.total}')
    def multiplicacion(self):
        self.total = self.numero1 * self.numero2
        print(f'La multiplicacion de {self.numero1} * {self.numero2} = {self.total}')
    def division(self):
        if self.numero2 == 0:
            print('Error la division no puede ser efectuada, no puedes tener un cero en el denominador, intentalo de nuevo')
        else:
            self.total = self.numero1 / self.numero2
            # la notacion :.3f se utiliza para establecer la cantidad de decimales que tendra nuestra respuesta, en este caso es de 3 decimales
            print(f'La division de {self.numero1} / {self.numero2} = {self.total:.3f}')

aritmetica = Aritmetica(10, 50)
aritmetica.suma()
aritmetica.resta()
aritmetica.multiplicacion()
aritmetica.division()
print()
print('------------------------------')

aritmetica2 = Aritmetica(30, 1)
aritmetica2.suma()
aritmetica2.resta()
aritmetica2.multiplicacion()
aritmetica2.division()