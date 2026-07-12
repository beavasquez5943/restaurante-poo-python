# Sistema de Gestión de Restaurante

## Estudiante

Bernardo Antonio Vasquez Maza

## Descripción

Este proyecto consiste en un sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos.

El sistema permite registrar productos y clientes mediante clases independientes organizadas en módulos.

## Estructura

```
restaurante_app/
│
├── modelos/
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py

## Constructor

La clase Producto utiliza el constructor __init__ para crear objetos a partir de los datos ingresados por el usuario.

## @property y @setter

Se utilizan para controlar el acceso y validar el nombre, la categoría y el precio de los productos.

## @dataclass

La clase Cliente fue desarrollada utilizando @dataclass para simplificar la creación de objetos.

## Menú

El sistema permite:

- Registrar productos
- Listar productos
- Buscar productos
- Registrar clientes
- Listar clientes
- Buscar clientes