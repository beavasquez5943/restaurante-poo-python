from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


restaurante = Restaurante()
archivo_servicio = ArchivoServicio()


# =====================================================
# CARGAR PRODUCTOS AL INICIAR
# =====================================================

restaurante.productos = archivo_servicio.cargar_productos()

print(
    f"\nSe cargaron {len(restaurante.productos)} "
    "producto(s) desde productos.json."
)


while True:

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Buscar producto")
    print("7. Buscar cliente")
    print("----------------------------------------")
    print("8. Actualizar producto")
    print("9. Eliminar producto")
    print("10. Salir")

    opcion = input("\nSeleccione una opción: ")


    # =================================================
    # REGISTRAR PRODUCTO
    # =================================================

    if opcion == "1":

        try:
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            disponible = input(
                "Disponible (s/n): "
            ).lower() == "s"

            producto = Producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponible
            )

            registrado = restaurante.registrar_producto(producto)

            if registrado:
                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except ValueError as e:
            print(f"\nError: {e}")


    # =================================================
    # REGISTRAR BEBIDA
    # =================================================

    elif opcion == "2":

        try:
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            tamano = input("Tamaño: ")

            disponible = input(
                "Disponible (s/n): "
            ).lower() == "s"

            bebida = Bebida(
                codigo,
                nombre,
                categoria,
                precio,
                tamano,
                disponible
            )

            registrado = restaurante.registrar_producto(bebida)

            if registrado:
                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except ValueError as e:
            print(f"\nError: {e}")


    # =================================================
    # REGISTRAR CLIENTE
    # =================================================

    elif opcion == "3":

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        try:
            cliente = Cliente(
                identificacion,
                nombre,
                correo
            )

            restaurante.registrar_cliente(cliente)

        except ValueError as e:
            print(f"\nError: {e}")


    # =================================================
    # LISTAR PRODUCTOS
    # =================================================

    elif opcion == "4":

        restaurante.listar_productos()


    # =================================================
    # LISTAR CLIENTES
    # =================================================

    elif opcion == "5":

        restaurante.listar_clientes()


    # =================================================
    # BUSCAR PRODUCTO
    # =================================================

    elif opcion == "6":

        codigo = input(
            "Código del producto: "
        )

        producto = restaurante.buscar_producto(codigo)

        if producto:
            print("----------------------------")
            print(producto.mostrar_informacion())
        else:
            print("\nProducto no encontrado.\n")


    # =================================================
    # BUSCAR CLIENTE
    # =================================================

    elif opcion == "7":

        identificacion = input(
            "Identificación del cliente: "
        )

        cliente = restaurante.buscar_cliente(
            identificacion
        )

        if cliente:
            print("----------------------------")
            print(cliente.mostrar_informacion())
        else:
            print("\nCliente no encontrado.\n")


    # =================================================
    # ACTUALIZAR PRODUCTO
    # =================================================

    elif opcion == "8":

        try:

            codigo = input(
                "Código del producto a actualizar: "
            )

            producto = restaurante.buscar_producto(codigo)

            if producto is None:
                print("\nProducto no encontrado.\n")
                continue

            nombre = input(
                f"Nuevo nombre [{producto.nombre}]: "
            )

            categoria = input(
                f"Nueva categoría [{producto.categoria}]: "
            )

            precio = float(
                input(
                    f"Nuevo precio [{producto.precio}]: "
                )
            )

            disponible = input(
                "Disponible (s/n): "
            ).lower() == "s"

            actualizado = restaurante.actualizar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponible
            )

            if actualizado:
                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except ValueError as e:
            print(f"\nError: {e}")


    # =================================================
    # ELIMINAR PRODUCTO
    # =================================================

    elif opcion == "9":

        codigo = input(
            "Código del producto a eliminar: "
        )

        eliminado = restaurante.eliminar_producto(
            codigo
        )

        if eliminado:
            archivo_servicio.guardar_productos(
                restaurante.productos
            )


    # =================================================
    # SALIR
    # =================================================

    elif opcion == "10":

        # Guardado final como respaldo
        archivo_servicio.guardar_productos(
            restaurante.productos
        )

        print(
            "\nGracias por utilizar el sistema."
        )

        break

    else:

        print("\nOpción inválida.\n")