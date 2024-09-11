import re
import math
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, scrolledtext
import pygame
import pyttsx3
import threading
import spacy
import speech_recognition as sr

# Inicialización de pygame para sonidos
pygame.init()
pygame.mixer.init()

# Inicialización del motor de voz
engine = pyttsx3.init()

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")

# Inicializar el reconocedor de voz
recognizer = sr.Recognizer()

class InterpreteAvanzado:
    def __init__(self):
        self.operaciones = {
            "suma": ["sumar", "añadir", "más", "plus"],
            "resta": ["restar", "quitar", "menos", "minus"],
            "multiplicacion": ["multiplicar", "por", "veces", "times"],
            "division": ["dividir", "entre", "sobre", "divide"]
        }

    def interpretar(self, comando):
        doc = nlp(comando.lower())
        numeros = [token.text for token in doc if token.like_num]
        if len(numeros) != 2:
            return None

        operacion = None
        for op, palabras_clave in self.operaciones.items():
            if any(palabra in comando.lower() for palabra in palabras_clave):
                operacion = op
                break

        if operacion:
            return operacion, float(numeros[0]), float(numeros[1])
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
                return f"El resultado de {operacion} {num1} y {num2} es: {resultado}"
            except ValueError as e:
                return str(e)
        else:
            return "No pude entender el comando. Por favor, intenta de nuevo."

class CalculadoraIAGUI:
    def __init__(self, master):
        self.master = master
        self.calculadora = Calculadora()
        self.interprete = InterpreteAvanzado()
        self.interfaz = InterfazUsuario(self.calculadora, self.interprete)

        master.title("Calculadora IA Avanzada con Voz")
        master.geometry("500x700")

        self.create_widgets()
        self.configurar_voz()

    def create_widgets(self):
        self.input_frame = ttk.Frame(self.master, padding="10")
        self.input_frame.pack(fill=tk.X)

        self.entrada = ttk.Entry(self.input_frame, width=50)
        self.entrada.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.boton_calcular = ttk.Button(self.input_frame, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(side=tk.RIGHT)

        self.boton_voz = ttk.Button(self.input_frame, text="Hablar", command=self.reconocer_voz)
        self.boton_voz.pack(side=tk.RIGHT)

        self.output_frame = ttk.Frame(self.master, padding="10")
        self.output_frame.pack(expand=True, fill=tk.BOTH)

        self.salida = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, width=50, height=20)
        self.salida.pack(expand=True, fill=tk.BOTH)

        self.entrada.bind('<Return>', lambda event: self.calcular())

        # Controles para la voz
        self.voice_frame = ttk.Frame(self.master, padding="10")
        self.voice_frame.pack(fill=tk.X)

        ttk.Label(self.voice_frame, text="Velocidad de voz:").pack(side=tk.LEFT)
        self.velocidad_voz = ttk.Scale(self.voice_frame, from_=100, to=200, orient=tk.HORIZONTAL, command=self.actualizar_voz)
        self.velocidad_voz.set(150)
        self.velocidad_voz.pack(side=tk.LEFT, expand=True, fill=tk.X)

        ttk.Label(self.voice_frame, text="Tono de voz:").pack(side=tk.LEFT)
        self.tono_voz = ttk.Scale(self.voice_frame, from_=50, to=150, orient=tk.HORIZONTAL, command=self.actualizar_voz)
        self.tono_voz.set(100)
        self.tono_voz.pack(side=tk.LEFT, expand=True, fill=tk.X)

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
        # Asegúrate de tener un archivo de sonido llamado "beep.wav" en el mismo directorio
        # pygame.mixer.Sound("beep.wav").play()
        pass

    def hablar(self, texto):
        def decir():
            engine.say(texto)
            engine.runAndWait()
        
        threading.Thread(target=decir).start()

    def configurar_voz(self):
        voices = engine.getProperty('voices')
        spanish_voice = next((voice for voice in voices if 'spanish' in voice.name.lower()), None)
        if spanish_voice:
            engine.setProperty('voice', spanish_voice.id)
        self.actualizar_voz()

    def actualizar_voz(self, *args):
        rate = int(self.velocidad_voz.get())
        pitch = self.tono_voz.get() / 100
        engine.setProperty('rate', rate)
        engine.setProperty('pitch', pitch)

    def reconocer_voz(self):
        with sr.Microphone() as source:
            self.salida.insert(tk.END, "Escuchando... Habla ahora.\n")
            self.salida.see(tk.END)
            audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, texto)
            self.salida.insert(tk.END, f"Has dicho: {texto}\n")
            self.salida.see(tk.END)
            self.calcular()
        except sr.UnknownValueError:
            self.salida.insert(tk.END, "No pude entender el audio\n")
            self.salida.see(tk.END)
        except sr.RequestError as e:
            self.salida.insert(tk.END, f"Error en el servicio de reconocimiento de voz; {e}\n")
            self.salida.see(tk.END)

def main():
    root = tk.Tk()
    app = CalculadoraIAGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
