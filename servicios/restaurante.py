from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra las colecciones y reglas del restaurante."""

    def __init__(self):
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        if self.buscar_producto(
            producto.codigo
        ) is not None:

            print(
                "\nError: Ya existe un producto "
                "con ese código.\n"
            )

            return False

        self.productos.append(producto)

        print(
            "\nProducto registrado correctamente.\n"
        )

        return True

    def listar_productos(self) -> None:

        if not self.productos:
            print(
                "\nNo existen productos registrados.\n"
            )
            return

        print(
            "\n===== LISTA DE PRODUCTOS ====="
        )

        for producto in self.productos:

            print(
                "----------------------------"
            )

            print(
                producto.mostrar_informacion()
            )

    def buscar_producto(
        self,
        codigo: str
    ):
        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(
            codigo
        )

        if producto is None:

            print(
                "\nProducto no encontrado.\n"
            )

            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        producto.disponible = (
            disponible and stock > 0
        )

        print(
            "\nProducto actualizado correctamente.\n"
        )

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(
            codigo
        )

        if producto is None:

            print(
                "\nProducto no encontrado.\n"
            )

            return False

        self.productos.remove(
            producto
        )

        print(
            "\nProducto eliminado correctamente.\n"
        )

        return True

    # =====================================================
    # USUARIOS
    # =====================================================

    def registrar_usuario(
        self,
        usuario: Usuario
    ) -> bool:

        for u in self.usuarios:

            if (
                u.identificacion
                == usuario.identificacion
            ):

                print(
                    "\nError: Ya existe un usuario "
                    "con esa identificación.\n"
                )

                return False

        self.usuarios.append(
            usuario
        )

        print(
            "\nUsuario registrado correctamente.\n"
        )

        return True

    def listar_usuarios(self) -> None:

        if not self.usuarios:

            print(
                "\nNo existen usuarios registrados.\n"
            )

            return

        print(
            "\n===== LISTA DE USUARIOS ====="
        )

        for usuario in self.usuarios:

            print(
                "----------------------------"
            )

            print(
                usuario.mostrar_informacion()
            )

    def buscar_usuario(
        self,
        identificacion: str
    ):

        for usuario in self.usuarios:

            if (
                usuario.identificacion
                == identificacion
            ):

                return usuario

        return None

    # =====================================================
    # VENTAS
    # =====================================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        # Validar usuario
        if usuario is None:

            print(
                "\nError: El usuario no existe.\n"
            )

            return False

        # Validar producto
        if producto is None:

            print(
                "\nError: El producto no existe.\n"
            )

            return False

        # Validar cantidad
        if cantidad <= 0:

            print(
                "\nError: La cantidad debe "
                "ser mayor que cero.\n"
            )

            return False

        # Validar stock
        if producto.stock < cantidad:

            print(
                f"\nError: Stock insuficiente. "
                f"Stock disponible: {producto.stock}.\n"
            )

            return False

        try:

            venta = Venta(
                usuario.identificacion,
                producto.codigo,
                cantidad
            )

            self._ventas.append(
                venta
            )

            producto.vender(
                cantidad
            )

            print(
                "\nVenta registrada correctamente.\n"
            )

            return True

        except ValueError as e:

            print(
                f"\nError al registrar la venta: {e}\n"
            )

            return False

    def obtener_ventas(
        self
    ) -> list[Venta]:

        return self._ventas.copy()

    # =====================================================
    # CONSULTA DE VENTAS POR USUARIO
    # =====================================================

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:

            if (
                venta.usuario_id
                == identificacion_usuario
            ):

                ventas_usuario.append(
                    venta
                )

        return ventas_usuario

    def mostrar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> None:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:

            print(
                "\nUsuario no encontrado.\n"
            )

            return

        ventas = self.consultar_ventas_usuario(
            identificacion_usuario
        )

        if not ventas:

            print(
                "\nEl usuario no tiene ventas "
                "registradas.\n"
            )

            return

        print(
            f"\n===== VENTAS DE "
            f"{usuario.nombre.upper()} ====="
        )

        for venta in ventas:

            producto = self.buscar_producto(
                venta.producto_codigo
            )

            if producto:

                nombre_producto = (
                    producto.nombre
                )

            else:

                nombre_producto = (
                    "Producto no disponible"
                )

            print(
                f"Producto: {nombre_producto} | "
                f"Código: {venta.producto_codigo} | "
                f"Cantidad: {venta.cantidad}"
            )