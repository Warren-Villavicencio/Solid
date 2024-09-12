class IScanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class MultiFunctionPrinter(IPrinter, IScanner):
    def print(self, document):
        print(document.content)

    def scan(self):
        # Simulación de escaneo
        print("Escaneando...")

# Cliente que necesita imprimir y escanear
multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print(document)
    multi_function_printer.scan()