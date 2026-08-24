import json
from pathlib import Path

from modelos.producto import Producto
from modelos.bebida import Bebida


class ArchivoServicio:
    """Gestiona la persistencia de productos y bebidas en JSON."""

    def __init__(
        self,
        ruta_archivo: str = "datos/productos.json"
    ):
        self.ruta_archivo = Path(ruta_archivo)

    def guardar_productos(self, productos: list[Producto]) -> None:
        """Guarda los productos en productos.json."""

        try:
            self.ruta_archivo.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            datos = [
                producto.to_dict()
                for producto in productos
            ]

            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print(
                "Error: no existen permisos suficientes "
                "para escribir productos.json."
            )

    def cargar_productos(self) -> list[Producto]:
        """Carga los productos y reconstruye sus objetos."""

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos = json.load(archivo)

        except FileNotFoundError:
            print(
                "Archivo productos.json no encontrado. "
                "Se iniciará con una colección vacía."
            )
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                "Error: no existen permisos suficientes "
                "para leer productos.json."
            )
            return []

        if not isinstance(datos, list):
            print(
                "Error: la estructura de productos.json "
                "debe ser una lista."
            )
            return []

        productos: list[Producto] = []

        for registro in datos:
            try:
                tipo = registro["tipo"]

                if tipo == "Bebida":
                    bebida = Bebida(
                        codigo=registro["codigo"],
                        nombre=registro["nombre"],
                        categoria=registro["categoria"],
                        precio=float(registro["precio"]),
                        tamano=registro["tamano"],
                        disponible=bool(
                            registro["disponible"]
                        )
                    )

                    productos.append(bebida)

                elif tipo == "Producto":
                    producto = Producto(
                        codigo=registro["codigo"],
                        nombre=registro["nombre"],
                        categoria=registro["categoria"],
                        precio=float(registro["precio"]),
                        disponible=bool(
                            registro["disponible"]
                        )
                    )

                    productos.append(producto)

                else:
                    print(
                        f"Advertencia: tipo '{tipo}' "
                        "no reconocido. Registro omitido."
                    )

            except KeyError as e:
                print(
                    f"Advertencia: falta la clave {e}. "
                    "El registro será omitido."
                )

            except ValueError as e:
                print(
                    f"Advertencia: registro inválido: {e}. "
                    "El registro será omitido."
                )

        return productos