from dataclasses import dataclass


@dataclass
class Usuario:
    """Representa a una persona registrada que puede realizar una compra."""

    identificacion: str
    nombre: str
    correo: str

    def __post_init__(self) -> None:
        if self.identificacion.strip() == "":
            raise ValueError("La identificación no puede estar vacía.")

        if self.nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")

        if self.correo.strip() == "":
            raise ValueError("El correo no puede estar vacío.")

    def to_dict(self) -> dict:
        """Convierte el usuario en un diccionario compatible con JSON."""

        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        """Reconstruye un objeto Usuario desde un diccionario."""

        return cls(
            identificacion=str(datos["identificacion"]),
            nombre=str(datos["nombre"]),
            correo=str(datos["correo"]),
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )