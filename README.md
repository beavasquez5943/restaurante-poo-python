# Sistema de Gestión de Restaurante - Semana 12

**Bernardo Antonio Vasquez Maza**

---

# Descripción del sistema

Este proyecto corresponde a la evolución del sistema `restaurante_app` desarrollado en Python mediante Programación Orientada a Objetos (POO).

El sistema permite gestionar productos, bebidas, usuarios y ventas mediante un menú interactivo ejecutado desde la consola.

La aplicación conserva la arquitectura modular desarrollada anteriormente y utiliza archivos JSON para almacenar productos, usuarios y ventas.

En esta versión correspondiente a la **Semana 12**, se optimizó el uso de colecciones para mejorar el rendimiento de las búsquedas y consultas frecuentes.

---

# Mejoras implementadas en Semana 12

Se conservaron las listas principales del sistema debido a que son útiles para:

- almacenar objetos;
- recorrer información;
- listar registros;
- persistir los datos en archivos JSON.

Además, se incorporaron índices auxiliares mediante diccionarios.

## Índice de productos

Se creó:

```python
self._productos_por_codigo