from dataclasses import dataclass

@dataclass
class Cliente:
    identificacion: str
    nombre: str
    correo: str

    def mostrar_informacion(self):
        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )