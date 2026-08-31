from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        disponible: bool = True,
        stock: int = 0,
    ):
        super().__init__(
            codigo,
            nombre,
            categoria,
            precio,
            disponible,
            stock,
        )

        self.tamano = tamano

    @property
    def tamano(self) -> str:
        return self.__tamano

    @tamano.setter
    def tamano(self, valor: str) -> None:
        if valor.strip() == "":
            raise ValueError("El tamaño no puede estar vacío.")

        self.__tamano = valor

    def to_dict(self) -> dict:
        """Convierte la bebida en un diccionario compatible con JSON."""

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "disponible": self.disponible,
            "stock": self.stock,
            "tamano": self.tamano,
            "tipo": "Bebida",
        }

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"Categoría: {self.categoria}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Tamaño: {self.tamano}\n"
            f"Stock: {self.stock}\n"
            f"Estado: {estado}"
        )