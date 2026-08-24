# servicios/restaurante.py

class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # =======================
    # PRODUCTOS
    # =======================

    def registrar_producto(self, producto) -> bool:
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("\nError: Ya existe un producto con ese código.\n")
                return False

        self.productos.append(producto)
        print("\nProducto registrado correctamente.\n")
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("\nNo existen productos registrados.\n")
            return

        print("\n===== LISTA DE PRODUCTOS =====")

        for producto in self.productos:
            print("----------------------------")
            print(producto.mostrar_informacion())

    def buscar_producto(self, codigo: str):
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
        disponible: bool
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            print("\nProducto no encontrado.\n")
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.disponible = disponible

        print("\nProducto actualizado correctamente.\n")
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            print("\nProducto no encontrado.\n")
            return False

        self.productos.remove(producto)

        print("\nProducto eliminado correctamente.\n")
        return True

    # =======================
    # CLIENTES
    # =======================

    def registrar_cliente(self, cliente) -> bool:
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print(
                    "\nError: Ya existe un cliente "
                    "con esa identificación.\n"
                )
                return False

        self.clientes.append(cliente)
        print("\nCliente registrado correctamente.\n")
        return True

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("\nNo existen clientes registrados.\n")
            return

        print("\n===== LISTA DE CLIENTES =====")

        for cliente in self.clientes:
            print("----------------------------")
            print(cliente.mostrar_informacion())

    def buscar_cliente(self, identificacion: str):
        for cliente in self.clientes:
            if cliente.identificacion == identificacion:
                return cliente

        return None