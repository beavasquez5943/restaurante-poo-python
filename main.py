# Importación de clases

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Andino")

# Crear productos
producto1 = Producto("Hamburguesa", 5.50, "Comida")
producto2 = Producto("Pizza", 8.00, "Comida")
producto3 = Producto("Jugo Natural", 2.50, "Bebida")

# Crear clientes
cliente1 = Cliente("Antonio Vasquez", "0102030405")
cliente2 = Cliente("Maria Lopez", "1102233445")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información registrada
restaurante.mostrar_informacion()