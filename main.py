# Archivo principal del proyecto

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante()
# Menu principal del sistema
while True:

    print("\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_=")
    print("      SISTEMA DE RESTAURANTE")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_=")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_=")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_=")
    print("7. Salir")

    opcion = input("\nSeleccione una opción: ")
# opcion registrar producto
    if opcion == "1":

        try:
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            disponible = input("Disponible (s/n): ").lower() == "s"

            producto = Producto(
                nombre,
                categoria,
                precio,
                disponible
            )

            restaurante.registrar_producto(producto)

            print("\nProducto registrado correctamente.")

        except ValueError as e:
            print(e)
# opcion listar productos
    elif opcion == "2":

        restaurante.listar_productos()
# opcion buscar producto
    elif opcion == "3":

        nombre = input("Ingrese el nombre del producto: ")

        producto = restaurante.buscar_producto(nombre)

        if producto:
            print(producto.mostrar_informacion())
        else:
            print("Producto no encontrado.")
# opcion registrar cliente
    elif opcion == "4":

        try:
            id_cliente = int(input("ID: "))
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            cliente = Cliente(
                id_cliente,
                nombre,
                correo
            )

            restaurante.registrar_cliente(cliente)

            print("Cliente registrado correctamente.")

        except ValueError:
            print("ID inválido.")
# opcion listar cliente
    elif opcion == "5":

        restaurante.listar_clientes()
# opcion buscar cliente
    elif opcion == "6":

        nombre = input("Nombre del cliente: ")

        cliente = restaurante.buscar_cliente(nombre)

        if cliente:
            print("----------------------------")
            print(f"ID: {cliente.id_cliente}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Correo: {cliente.correo}")
        else:
            print("Cliente no encontrado.")
# opcion salir
    elif opcion == "7":

        print("\nGracias por utilizar el sistema.")
        break

    else:

        print("Opción inválida.")