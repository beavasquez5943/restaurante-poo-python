# Clase que representa un producto del restaurante
class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        if valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (f"Nombre: {self.nombre}\n"
                f"Categoría: {self.categoria}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Estado: {estado}")