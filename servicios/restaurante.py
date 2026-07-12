class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    # Productos

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("\nNo existen productos registrados.\n")
            return

        for producto in self.productos:
            print("----------------------------")
            print(producto.mostrar_informacion())

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # Clientes

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("\nNo existen clientes registrados.\n")
            return

        for cliente in self.clientes:
            print("----------------------------")
            print(f"ID: {cliente.id_cliente}")
            print(f"Nombre: {cliente.nombre}")
            print(f"Correo: {cliente.correo}")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None