from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

class Document:
    def __init__(self, content):
        self.content = content

class ConcretePrinter(IPrinter):
    def print(self, document):
        print(document.content)

# Cliente que solo necesita imprimir
document = Document("Hola, mundo!")
printer = ConcretePrinter()
printer.print(document)