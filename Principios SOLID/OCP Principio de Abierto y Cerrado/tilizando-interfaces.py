from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        import math
        return math.pi * self.radio**2

# Para agregar una nueva forma, creamos una nueva clase que implemente la interfaz Forma
class Triangulo(Forma):
    # ... implementación del cálculo del área del triángulo ...