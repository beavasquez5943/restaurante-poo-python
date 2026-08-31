from pathlib import Path

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario

from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


BASE_DIR = Path(__file__).resolve().parent

restaurante = Restaurante()

archivo_servicio = ArchivoServicio(
    str(BASE_DIR / "datos")
)


# =====================================================
# CARGAR COLECCIONES AL INICIAR
# =====================================================

try:

    restaurante.productos = (
        archivo_servicio.cargar_productos()
    )

    restaurante.usuarios = (
        archivo_servicio.cargar_usuarios()
    )

    restaurante._ventas = (
        archivo_servicio.cargar_ventas()
    )

    print(
        f"\nSe cargaron "
        f"{len(restaurante.productos)} producto(s), "
        f"{len(restaurante.usuarios)} usuario(s) y "
        f"{len(restaurante._ventas)} venta(s)."
    )

except (
    ValueError,
    PermissionError
) as e:

    print(
        f"\nError al cargar los datos: {e}"
    )


while True:

    print(
        "\n========================================"
    )

    print(
        "        SISTEMA DE RESTAURANTE"
    )

    print(
        "========================================"
    )

    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar usuario")

    print(
        "----------------------------------------"
    )

    print("4. Listar productos")
    print("5. Listar usuarios")

    print(
        "----------------------------------------"
    )

    print("6. Buscar producto")
    print("7. Buscar usuario")

    print(
        "----------------------------------------"
    )

    print("8. Actualizar producto")
    print("9. Eliminar producto")

    print("10. Registrar venta")
    print("11. Consultar ventas de un usuario")

    print("12. Salir")


    opcion = input(
        "\nSeleccione una opción: "
    )


    # =================================================
    # REGISTRAR PRODUCTO
    # =================================================

    if opcion == "1":

        try:

            codigo = input(
                "Código: "
            )

            nombre = input(
                "Nombre: "
            )

            categoria = input(
                "Categoría: "
            )

            precio = float(
                input("Precio: ")
            )

            stock = int(
                input("Stock: ")
            )

            disponible = stock > 0

            producto = Producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponible,
                stock
            )

            registrado = (
                restaurante.registrar_producto(
                    producto
                )
            )

            if registrado:

                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except (
            ValueError,
            PermissionError
        ) as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # REGISTRAR BEBIDA
    # =================================================

    elif opcion == "2":

        try:

            codigo = input(
                "Código: "
            )

            nombre = input(
                "Nombre: "
            )

            categoria = input(
                "Categoría: "
            )

            precio = float(
                input("Precio: ")
            )

            tamano = input(
                "Tamaño: "
            )

            stock = int(
                input("Stock: ")
            )

            disponible = stock > 0

            bebida = Bebida(
                codigo,
                nombre,
                categoria,
                precio,
                tamano,
                disponible,
                stock
            )

            registrado = (
                restaurante.registrar_producto(
                    bebida
                )
            )

            if registrado:

                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except (
            ValueError,
            PermissionError
        ) as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # REGISTRAR USUARIO
    # =================================================

    elif opcion == "3":

        try:

            identificacion = input(
                "Identificación: "
            )

            nombre = input(
                "Nombre: "
            )

            correo = input(
                "Correo: "
            )

            usuario = Usuario(
                identificacion,
                nombre,
                correo
            )

            registrado = (
                restaurante.registrar_usuario(
                    usuario
                )
            )

            if registrado:

                archivo_servicio.guardar_usuarios(
                    restaurante.usuarios
                )

        except (
            ValueError,
            PermissionError
        ) as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # LISTAR PRODUCTOS
    # =================================================

    elif opcion == "4":

        restaurante.listar_productos()


    # =================================================
    # LISTAR USUARIOS
    # =================================================

    elif opcion == "5":

        restaurante.listar_usuarios()


    # =================================================
    # BUSCAR PRODUCTO
    # =================================================

    elif opcion == "6":

        codigo = input(
            "Código del producto: "
        )

        producto = restaurante.buscar_producto(
            codigo
        )

        if producto:

            print(
                "----------------------------"
            )

            print(
                producto.mostrar_informacion()
            )

        else:

            print(
                "\nProducto no encontrado.\n"
            )


    # =================================================
    # BUSCAR USUARIO
    # =================================================

    elif opcion == "7":

        identificacion = input(
            "Identificación del usuario: "
        )

        usuario = restaurante.buscar_usuario(
            identificacion
        )

        if usuario:

            print(
                "----------------------------"
            )

            print(
                usuario.mostrar_informacion()
            )

        else:

            print(
                "\nUsuario no encontrado.\n"
            )


    # =================================================
    # ACTUALIZAR PRODUCTO
    # =================================================

    elif opcion == "8":

        try:

            codigo = input(
                "Código del producto a actualizar: "
            )

            producto = restaurante.buscar_producto(
                codigo
            )

            if producto is None:

                print(
                    "\nProducto no encontrado.\n"
                )

                continue

            nombre = input(
                f"Nuevo nombre "
                f"[{producto.nombre}]: "
            )

            categoria = input(
                f"Nueva categoría "
                f"[{producto.categoria}]: "
            )

            precio = float(
                input(
                    f"Nuevo precio "
                    f"[{producto.precio}]: "
                )
            )

            stock = int(
                input(
                    f"Nuevo stock "
                    f"[{producto.stock}]: "
                )
            )

            disponible = stock > 0

            actualizado = (
                restaurante.actualizar_producto(
                    codigo,
                    nombre,
                    categoria,
                    precio,
                    disponible,
                    stock
                )
            )

            if actualizado:

                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except (
            ValueError,
            PermissionError
        ) as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # ELIMINAR PRODUCTO
    # =================================================

    elif opcion == "9":

        try:

            codigo = input(
                "Código del producto a eliminar: "
            )

            eliminado = (
                restaurante.eliminar_producto(
                    codigo
                )
            )

            if eliminado:

                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except PermissionError as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # REGISTRAR VENTA
    # =================================================

    elif opcion == "10":

        try:

            identificacion = input(
                "Identificación del usuario: "
            )

            codigo = input(
                "Código del producto: "
            )

            cantidad = int(
                input("Cantidad: ")
            )

            realizada = (
                restaurante.vender_producto(
                    codigo,
                    identificacion,
                    cantidad
                )
            )

            if realizada:

                archivo_servicio.guardar_ventas(
                    restaurante.obtener_ventas()
                )

                archivo_servicio.guardar_productos(
                    restaurante.productos
                )

        except (
            ValueError,
            PermissionError
        ) as e:

            print(
                f"\nError: {e}"
            )


    # =================================================
    # CONSULTAR VENTAS POR USUARIO
    # =================================================

    elif opcion == "11":

        identificacion = input(
            "Identificación del usuario: "
        )

        restaurante.mostrar_ventas_usuario(
            identificacion
        )


    # =================================================
    # SALIR
    # =================================================

    elif opcion == "12":

        try:

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            archivo_servicio.guardar_usuarios(
                restaurante.usuarios
            )

            archivo_servicio.guardar_ventas(
                restaurante.obtener_ventas()
            )

        except PermissionError as e:

            print(
                f"\nError al guardar los datos: {e}"
            )

        print(
            "\nGracias por utilizar el sistema."
        )

        break


    else:

        print(
            "\nOpción inválida.\n"
        )