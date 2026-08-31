# Sistema de Gestión de Restaurante


**Bernardo Antonio Vasquez Maza**

---

# Descripción del sistema

Este proyecto consiste en un sistema de gestión de restaurante desarrollado en Python mediante Programación Orientada a Objetos (POO). El sistema permite registrar y listar productos, bebidas y clientes a través de un menú interactivo ejecutado desde la consola.

La aplicación fue organizada en módulos independientes para mantener una estructura clara y facilitar el mantenimiento del código, aplicando los principios SOLID solicitados en la actividad.

---

# Estructura del proyecto


restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md


# Responsabilidad de cada clase

# Producto

Representa un producto del restaurante. Contiene la información general como código, nombre, categoría, precio y disponibilidad.

# Bebida

Hereda de la clase Producto e incorpora un atributo adicional denominado tamaño. Sobrescribe el método `mostrar_informacion()` para mostrar también esta información.

# Cliente

Representa la información de un cliente registrado mediante su identificación, nombre y correo electrónico.

# Restaurante

Administra las colecciones de productos y clientes. También realiza el registro, búsqueda, listado y validación de códigos e identificaciones duplicadas.

# main.py

Es el punto de entrada del programa. Muestra el menú interactivo, solicita los datos al usuario y llama a los métodos de la clase Restaurante.



# Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, ya que una bebida representa un tipo de producto dentro del restaurante.

Gracias a la herencia, una bebida puede utilizar todas las características de un producto y añadir información específica sin modificar la estructura existente del sistema.



# Principios SOLID aplicados

## SRP (Responsabilidad Única)

Cada clase tiene una única responsabilidad:

* Producto representa productos.
* Bebida representa bebidas.
* Cliente representa clientes.
* Restaurante administra la información.
* main.py gestiona únicamente la interacción con el usuario.

## OCP (Abierto/Cerrado)

El sistema fue ampliado mediante la creación de la clase Bebida sin modificar la lógica principal de la clase Restaurante.

## LSP (Sustitución de Liskov)

Los objetos de la clase Bebida pueden utilizarse como objetos Producto. Ambos pueden almacenarse en la misma colección y utilizan el método `mostrar_informacion()` mediante polimorfismo.

---

# Instrucciones de ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Verificar que la estructura de carpetas sea correcta.
3. Ejecutar el archivo `main.py`.
4. Utilizar el menú para registrar productos, bebidas y clientes.
5. Probar las opciones de búsqueda y listado.

---

# Reflexión

La aplicación de los principios SOLID permite desarrollar programas más organizados, fáciles de mantener y de ampliar. La separación de responsabilidades facilita la comprensión del código y la incorporación de nuevas funcionalidades sin afectar el funcionamiento existente del sistema. Además, el uso de herencia y polimorfismo mejora la reutilización del código y promueve buenas prácticas de Programación Orientada a Objetos.
