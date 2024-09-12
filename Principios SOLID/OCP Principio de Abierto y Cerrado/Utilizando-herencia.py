class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass  # Método abstracto

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

# Para agregar un nuevo animal, creamos una nueva clase que herede de Animal
class Caballo(Animal):
    def hablar(self):
        print("Hiii!")