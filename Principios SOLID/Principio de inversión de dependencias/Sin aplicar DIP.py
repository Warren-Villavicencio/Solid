class EmailSender:
    def send_email(self, to, subject, body):
        # Código para enviar un email usando un servicio de correo específico (e.g., Gmail)
        pass

class CustomerController:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_welcome_email(self, customer):
        self.email_sender.send_email(customer.email, "Bienvenido", "Mensaje de bienvenida")