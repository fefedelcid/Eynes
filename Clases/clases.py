'''
Escribir una clase en python llamada círculo que contenga un radio,
con un método que devuelva el área y otro que devuelva
el perímetro del círculo. Si se instancia la clase con radio <= 0
mostrar una excepción indicando un error amigable al usuario e impidiendo
la instanciación.
'''
from math import pi

class Circulo:
    def __init__(self, radio):
        if type(radio) not in [int, float]:
            raise TypeError(f"{type(radio)} no es un tipo de radio válido.")
        elif radio <= 0:
            raise ValueError('El radio debe ser mayor que 0.')
        else:
            self.radio = radio


    def area(self):
        return pi*(self.radio**2)


    def perimetro(self):
        return 2*pi*self.radio
