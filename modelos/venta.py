from dataclasses import dataclass


@dataclass
class Venta:
    """Representa una venta y relaciona un usuario con un producto."""

    usuario_id: str
    producto_codigo: str
    cantidad: int

    def __post_init__(self) -> None:
        if self.usuario_id.strip() == "":
            raise ValueError(
                "La identificación del usuario no puede estar vacía."
            )

        if self.producto_codigo.strip() == "":
            raise ValueError(
                "El código del producto no puede estar vacío."
            )

        if self.cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

    def to_dict(self) -> dict:
        """Convierte la venta a un diccionario compatible con JSON."""

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        """Reconstruye una Venta desde un diccionario."""

        return cls(
            usuario_id=str(datos["usuario_id"]),
            producto_codigo=str(datos["producto_codigo"]),
            cantidad=int(datos["cantidad"]),
        )