# modelos/producto.py
class Producto:
    """Clase que representa un producto del restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool = True,
        stock: int = 0,
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.disponible = disponible

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if valor.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self.__codigo = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = valor

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if isinstance(valor, bool) or int(valor) != valor:
            raise ValueError("El stock debe ser un número entero.")

        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.__stock = int(valor)

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock cuando se realiza una venta válida."""

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.stock:
            raise ValueError("Stock insuficiente.")

        self.stock -= cantidad

        if self.stock == 0:
            self.disponible = False

    def to_dict(self) -> dict:
        """Convierte el producto a una estructura compatible con JSON."""

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "disponible": self.disponible,
            "stock": self.stock,
            "tipo": "Producto",
        }

    def mostrar_informacion(self) -> str:
        """Devuelve la información del producto."""

        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock}\n"
            f"Estado: {estado}"
        )