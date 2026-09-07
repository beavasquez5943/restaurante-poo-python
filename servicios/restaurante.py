from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """Administra las colecciones y reglas del restaurante."""

    def __init__(self):
        # Colecciones principales
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        # Índices auxiliares para mejorar el rendimiento
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

    # =====================================================
    # ÍNDICES
    # =====================================================

    def reconstruir_indices(self) -> None:
        """
        Reconstruye los índices a partir de las colecciones
        principales después de cargar los datos desde JSON.
        """

        self._productos_por_codigo = {
            producto.codigo: producto
            for producto in self.productos
        }

        self._usuarios_por_identificacion = {
            usuario.identificacion: usuario
            for usuario in self.usuarios
        }

        self._ventas_por_usuario = {}

        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(
                venta.usuario_id,
                []
            ).append(venta)

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def registrar_producto(
        self,
        producto: Producto
    ) -> bool:

        # La búsqueda de duplicados utiliza el índice
        if producto.codigo in self._productos_por_codigo:
            print(
                "\nError: Ya existe un producto "
                "con ese código.\n"
            )
            return False

        self.productos.append(producto)

        # Mantener sincronizado el índice
        self._productos_por_codigo[producto.codigo] = producto

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
        """
        Busca directamente un producto mediante
        el índice por código.
        """

        return self._productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        disponible: bool,
        stock: int
    ) -> bool:

        # Búsqueda optimizada mediante diccionario
        producto = self._productos_por_codigo.get(
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

        # El código no cambia, pero se mantiene
        # explícitamente sincronizado.
        self._productos_por_codigo[codigo] = producto

        print(
            "\nProducto actualizado correctamente.\n"
        )

        return True

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        # Búsqueda mediante índice
        producto = self._productos_por_codigo.get(
            codigo
        )

        if producto is None:
            print(
                "\nProducto no encontrado.\n"
            )
            return False

        # Eliminar de la colección principal
        self.productos.remove(producto)

        # Eliminar también del índice
        self._productos_por_codigo.pop(
            codigo,
            None
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

        # Validación mediante índice
        if (
            usuario.identificacion
            in self._usuarios_por_identificacion
        ):
            print(
                "\nError: Ya existe un usuario "
                "con esa identificación.\n"
            )
            return False

        self.usuarios.append(usuario)

        # Mantener actualizado el índice
        self._usuarios_por_identificacion[
            usuario.identificacion
        ] = usuario

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
        """
        Busca directamente un usuario mediante
        el índice por identificación.
        """

        return self._usuarios_por_identificacion.get(
            identificacion
        )

    # =====================================================
    # VENTAS
    # =====================================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        # Buscar usuario mediante índice
        usuario = (
            self._usuarios_por_identificacion.get(
                identificacion_usuario
            )
        )

        # Buscar producto mediante índice
        producto = (
            self._productos_por_codigo.get(
                codigo_producto
            )
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

            # Agregar a la colección principal
            self._ventas.append(venta)

            # Actualizar índice de ventas por usuario
            self._ventas_por_usuario.setdefault(
                usuario.identificacion,
                []
            ).append(venta)

            # Actualizar stock
            producto.vender(cantidad)

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

        """
        Consulta las ventas de un usuario utilizando
        el índice _ventas_por_usuario, evitando recorrer
        toda la lista de ventas.
        """

        return self._ventas_por_usuario.get(
            identificacion_usuario,
            []
        ).copy()

    def mostrar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> None:

        # Buscar usuario mediante índice
        usuario = (
            self._usuarios_por_identificacion.get(
                identificacion_usuario
            )
        )

        if usuario is None:
            print(
                "\nUsuario no encontrado.\n"
            )
            return

        # Obtener ventas mediante índice
        ventas = (
            self._ventas_por_usuario.get(
                identificacion_usuario,
                []
            )
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

            # Búsqueda del producto mediante índice
            producto = (
                self._productos_por_codigo.get(
                    venta.producto_codigo
                )
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