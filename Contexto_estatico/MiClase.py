class MiClase():
    
    #Esta variable de tipo clase, se va a compartir con cualquier tipo de objeto, en pocas palabras los objetos acceden a la misma referencia de clase
    variable_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    #no utilizamos el metodo self en nuestro metodo estatico, debido a que no son posibles instanciarlo con las funciones de clase que estan relacionadas a los objetos
    @staticmethod
    def metodo_estatico():
    #No podemos acceder al meotodo de instancia self por lo tanto no podemos especificar atributos de tipo objeto en las clases estaticas
    # self.variable_instancia
    #Tenemos que acceder a los objetos atraves de la clases
        print(MiClase.variable_clase)

#print(MiClase.variable_clase)
#miClase = MiClase('Variable de instancia')
#print(miClase.variable_instancia)

MiClase.metodo_estatico()