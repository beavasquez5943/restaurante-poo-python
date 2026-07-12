# Clase que representa un cliente
from dataclasses import dataclass

@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str
