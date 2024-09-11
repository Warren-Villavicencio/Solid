import re
import math
from abc import ABC, abstractmethod

# Principio de Responsabilidad Única (S)
class Interprete:
    def interpretar(self, comando):
        # Aquí iría la lógica de interpretación del lenguaje natural
        # Por ahora, usaremos una versión simplificada
        match = re.match(r'(\w+)\s+([\d.]+)\s+([\d.]+)', comando)
        if match:
            operacion, num1, num2 = match.groups()
            return operacion, float(num1), float(num2)
        else:
            return None

# Principio de Abierto/Cerrado (O)
class OperacionBase(ABC):
    @abstractmethod
    def ejecutar(self, a, b):
        pass

class Suma(OperacionBase):
    def ejecutar(self, a, b):
        return a + b

class Resta(OperacionBase):
    def ejecutar(self, a, b):
        return a - b

class Multiplicacion(OperacionBase):
    def ejecutar(self, a, b):
        return a * b

class Division(OperacionBase):
    def ejecutar(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("No se puede dividir por cero")

# Principio de Sustitución de Liskov (L)
class Calculadora:
    def __init__(self):
        self.operaciones = {
            'suma': Suma(),
            'resta': Resta(),
            'multiplicacion': Multiplicacion(),
            'division': Division()
        }

    def calcular(self, operacion, a, b):
        if operacion in self.operaciones:
            return self.operaciones[operacion].ejecutar(a, b)
        else:
            raise ValueError(f"Operación no soportada: {operacion}")

# Principio de Segregación de Interfaces (I)
class InterfazUsuario:
    def __init__(self, calculadora, interprete):
        self.calculadora = calculadora
        self.interprete = interprete

    def procesar_comando(self, comando):
        interpretacion = self.interprete.interpretar(comando)
        if interpretacion:
            operacion, num1, num2 = interpretacion
            try:
                resultado = self.calculadora.calcular(operacion, num1, num2)
                return f"El resultado es: {resultado}"
            except ValueError as e:
                return str(e)
        else:
            return "No pude entender el comando. Por favor, intenta de nuevo."

# Principio de Inversión de Dependencias (D)
class CalculadoraIA:
    def __init__(self):
        self.calculadora = Calculadora()
        self.interprete = Interprete()
        self.interfaz = InterfazUsuario(self.calculadora, self.interprete)

    def ejecutar(self):
        print("Bienvenido a la Calculadora IA")
        print("Puedes realizar operaciones como: 'suma 5 3' o 'multiplicacion 4 2'")
        while True:
            comando = input("Ingresa tu comando (o 'salir' para terminar): ")
            if comando.lower() == 'salir':
                break
            resultado = self.interfaz.procesar_comando(comando)
            print(resultado)

if __name__ == "__main__":
    calc_ia = CalculadoraIA()
    calc_ia.ejecutar()