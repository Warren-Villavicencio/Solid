class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_precio_con_descuento(self, porcentaje):
        # Calcula el precio con descuento
        return self.precio * (1 - porcentaje / 100)

class RepositorioProducto:
    def guardar(self, producto):
        # Guarda el producto en la base de datos
        # ...

class VistaProducto:
    def mostrar_detalles(self, producto):
        # Muestra los detalles del producto
        print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")