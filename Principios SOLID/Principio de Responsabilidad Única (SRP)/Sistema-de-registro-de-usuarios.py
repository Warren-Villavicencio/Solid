class Usuario:
    def __init__(self, nombre, email, contrasena):
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena

    def registrarse(self):
        # Valida los datos
        # Envia un correo de confirmación
        # Guarda el usuario en la base de datos
        # ...