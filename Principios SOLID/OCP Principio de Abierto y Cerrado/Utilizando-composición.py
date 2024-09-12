class Motor:
    def arrancar(self):
        print("Arrancando motor...")

class Coche:
    def __init__(self, motor):
        self.motor = motor

    def conducir(self):
        self.motor.arrancar()
        print("Conduciendo...")