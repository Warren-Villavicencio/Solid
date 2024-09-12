class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} {self.apellido}")

    def calcular_impuestos(self, salario):
        # Lógica para calcular impuestos
        pass