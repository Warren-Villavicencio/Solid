from abc import ABC, abstractmethod

class EmailSenderInterface(ABC):
    @abstractmethod
    def send_email(self, to, subject, body):
        pass

class GmailSender(EmailSenderInterface):
    def send_email(self, to, subject, body):
        # Código para enviar un email usando Gmail
        pass

class CustomerController:
    def __init__(self, email_sender: EmailSenderInterface):
        self.email_sender = email_sender

    def send_welcome_email(self, customer):
        self.email_sender.send_email(customer.email, "Bienvenido", "Mensaje de bienvenida")