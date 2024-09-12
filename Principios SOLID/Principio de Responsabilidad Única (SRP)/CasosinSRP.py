class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_descuento(self, porcentaje):
        # Calcula el descuento
        self.precio *= (1 - porcentaje / 100)

    def guardar_en_base_datos(self):
        # Guarda el producto en la base de datos
        # ...

    def mostrar_detalles(self):
        # Muestra los detalles del producto
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")