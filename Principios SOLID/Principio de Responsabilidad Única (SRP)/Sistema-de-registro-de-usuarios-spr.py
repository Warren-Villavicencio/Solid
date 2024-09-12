class ValidadorUsuario:
    def validar(self, usuario):
        # Valida los datos del usuario
        # ...

class EnvioCorreo:
    def enviar_correo_confirmacion(self, email):
        # Envia un correo de confirmación
        # ...

class RepositorioUsuario:
    def guardar(self, usuario):
        # Guarda el usuario en la base de datos
        # ...

class ServicioRegistro:
    def registrar(self, nombre, email, contrasena):
        usuario = Usuario(nombre, email, contrasena)
        validador = ValidadorUsuario()
        validador.validar(usuario)
        envia_correo = EnvioCorreo()
        envia_correo.enviar_correo_confirmacion(usuario.email)
        repositorio = RepositorioUsuario()
        repositorio.guardar(usuario)