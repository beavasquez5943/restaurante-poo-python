# Clase que representa un cliente

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"