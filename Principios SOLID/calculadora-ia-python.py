import re
import math
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, scrolledtext
import pygame
import pyttsx3
import threading

# Inicialización de pygame para sonidos
pygame.init()
pygame.mixer.init()

# Inicialización del motor de voz
engine = pyttsx3.init()

# Cargar sonido (asegúrate de tener un archivo de sonido en la misma carpeta)
# pygame.mixer.Sound("beep.wav")

class Interprete:
    def interpretar(self, comando):
        match = re.match(r'(\w+)\s+([\d.]+)\s+([\d.]+)', comando)
        if match:
            operacion, num1, num2 = match.groups()
            return operacion, float(num1), float(num2)
        else:
            return None

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

class CalculadoraIAGUI:
    def __init__(self, master):
        self.master = master
        self.calculadora = Calculadora()
        self.interprete = Interprete()
        self.interfaz = InterfazUsuario(self.calculadora, self.interprete)

        master.title("Calculadora IA")
        master.geometry("400x500")

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = ttk.Frame(self.master, padding="10")
        self.input_frame.pack(fill=tk.X)

        self.entrada = ttk.Entry(self.input_frame, width=50)
        self.entrada.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.boton_calcular = ttk.Button(self.input_frame, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(side=tk.RIGHT)

        self.output_frame = ttk.Frame(self.master, padding="10")
        self.output_frame.pack(expand=True, fill=tk.BOTH)

        self.salida = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=50, height=20)
        self.salida.pack(expand=True, fill=tk.BOTH)

        self.entrada.bind('<Return>', lambda event: self.calcular())

    def calcular(self):
        comando = self.entrada.get()
        resultado = self.interfaz.procesar_comando(comando)
        self.mostrar_resultado(resultado)
        self.entrada.delete(0, tk.END)

    def mostrar_resultado(self, resultado):
        self.salida.insert(tk.END, f"{resultado}\n")
        self.salida.see(tk.END)
        self.reproducir_sonido()
        self.hablar(resultado)

    def reproducir_sonido(self):
        # Descomentar la siguiente línea si tienes un archivo de sonido
        # pygame.mixer.Sound("beep.wav").play()
        pass

    def hablar(self, texto):
        def decir():
            engine.say(texto)
            engine.runAndWait()
        
        # Ejecutar la síntesis de voz en un hilo separado para no bloquear la GUI
        threading.Thread(target=decir).start()

def main():
    root = tk.Tk()
    app = CalculadoraIAGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
