class Color():
    def __init__(self, color):
        self._color = color
        #Propiedades getter and setter
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    