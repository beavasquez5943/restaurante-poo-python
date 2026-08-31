import json
from pathlib import Path

from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    """Gestiona la persistencia de productos, usuarios y ventas."""

    def __init__(self, carpeta_datos: str = "datos"):
        self.carpeta_datos = Path(carpeta_datos)

        self.carpeta_datos.mkdir(
            parents=True,
            exist_ok=True
        )

        self.ruta_productos = (
            self.carpeta_datos / "productos.json"
        )

        self.ruta_usuarios = (
            self.carpeta_datos / "usuarios.json"
        )

        self.ruta_ventas = (
            self.carpeta_datos / "ventas.json"
        )

    def _guardar(
        self,
        datos: list[dict],
        ruta: Path
    ) -> None:

        try:
            ruta.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError as e:
            raise PermissionError(
                f"No hay permisos para escribir {ruta.name}."
            ) from e

    def _cargar(self, ruta: Path) -> list[dict]:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

        except FileNotFoundError:
            print(
                f"Archivo {ruta.name} no encontrado. "
                "Se iniciará con una colección vacía."
            )

            return []

        except json.JSONDecodeError as e:
            raise ValueError(
                f"{ruta.name} contiene JSON inválido."
            ) from e

        except PermissionError as e:
            raise PermissionError(
                f"No hay permisos para leer {ruta.name}."
            ) from e

        if not isinstance(datos, list):
            raise ValueError(
                f"La estructura de {ruta.name} "
                "debe ser una lista."
            )

        return datos

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> None:

        datos = [
            producto.to_dict()
            for producto in productos
        ]

        self._guardar(
            datos,
            self.ruta_productos
        )

    def cargar_productos(self) -> list[Producto]:

        productos: list[Producto] = []

        for registro in self._cargar(
            self.ruta_productos
        ):
            try:
                tipo = registro["tipo"]

                stock = int(
                    registro.get("stock", 0)
                )

                if stock < 0:
                    raise ValueError(
                        "El stock no puede ser negativo."
                    )

                if tipo == "Bebida":

                    producto = Bebida(
                        codigo=registro["codigo"],
                        nombre=registro["nombre"],
                        categoria=registro["categoria"],
                        precio=float(
                            registro["precio"]
                        ),
                        tamano=registro["tamano"],
                        disponible=bool(
                            registro["disponible"]
                        ),
                        stock=stock,
                    )

                elif tipo == "Producto":

                    producto = Producto(
                        codigo=registro["codigo"],
                        nombre=registro["nombre"],
                        categoria=registro["categoria"],
                        precio=float(
                            registro["precio"]
                        ),
                        disponible=bool(
                            registro["disponible"]
                        ),
                        stock=stock,
                    )

                else:
                    print(
                        f"Advertencia: tipo '{tipo}' "
                        "no reconocido. Registro omitido."
                    )

                    continue

                productos.append(producto)

            except (
                KeyError,
                TypeError,
                ValueError
            ) as e:

                print(
                    f"Advertencia: registro de producto "
                    f"inválido: {e}. Registro omitido."
                )

        return productos

    # =====================================================
    # USUARIOS
    # =====================================================

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:

        datos = [
            usuario.to_dict()
            for usuario in usuarios
        ]

        self._guardar(
            datos,
            self.ruta_usuarios
        )

    def cargar_usuarios(self) -> list[Usuario]:

        usuarios: list[Usuario] = []

        for registro in self._cargar(
            self.ruta_usuarios
        ):
            try:
                usuario = Usuario.from_dict(
                    registro
                )

                usuarios.append(usuario)

            except (
                KeyError,
                TypeError,
                ValueError
            ) as e:

                print(
                    f"Advertencia: registro de usuario "
                    f"inválido: {e}. Registro omitido."
                )

        return usuarios

    # =====================================================
    # VENTAS
    # =====================================================

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:

        datos = [
            venta.to_dict()
            for venta in ventas
        ]

        self._guardar(
            datos,
            self.ruta_ventas
        )

    def cargar_ventas(self) -> list[Venta]:

        ventas: list[Venta] = []

        for registro in self._cargar(
            self.ruta_ventas
        ):
            try:
                venta = Venta.from_dict(
                    registro
                )

                ventas.append(venta)

            except (
                KeyError,
                TypeError,
                ValueError
            ) as e:

                print(
                    f"Advertencia: registro de venta "
                    f"inválido: {e}. Registro omitido."
                )

        return ventas