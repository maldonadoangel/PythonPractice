class MiClase():
    
    #Esta variable de tipo clase, se va a compartir con cualquier tipo de objeto, en pocas palabras los objetos acceden a la misma referencia de clase
    variable_clase = 'Valor variable clase'
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)
miClase = MiClase('Variable de instancia')
print(miClase.variable_instancia)