# Archivo principal del proyecto

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main():

    # Crear restaurante
    restaurante = Restaurante("Restaurante Sabor Andino")

    # Crear productos

    producto1 = Producto(
        "Pizza Familiar",
        "Comida",
        15.99,
        12,
        True
    )

    producto2 = Producto(
        "Jugo Natural",
        "Bebida",
        3.50,
        25,
        True
    )

    # Crear clientes

    cliente1 = Cliente(
        "Antonio Vasquez",
        22,
        "antonio@email.com",
        True
    )

    cliente2 = Cliente(
        "María López",
        28,
        "maria@email.com",
        False
    )

    # Agregar productos

    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)

    # Agregar clientes

    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)

    # Mostrar información

    print("=" * 50)
    print(restaurante.nombre)
    print("=" * 50)

    restaurante.mostrar_productos()
    restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()