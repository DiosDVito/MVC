from Model.DAO.prestamo_dao import PrestamoDAO
from Model.DAO.libro_dao import LibroDAO
from Model.Objects.prestamo import Prestamo
import uuid
from datetime import date

class PrestamoController:
    def __init__(self, usuario_actual):
        self.view = None
        self.usuario_actual = usuario_actual
        self.prestamo_dao = PrestamoDAO()
        self.libro_dao = LibroDAO()  # Para leer/actualizar libros

    def set_view(self, view):
        self.view = view

    def load_prestamos(self):
        """
        Carga todos los préstamos o filtra por user_id si es estudiante.
        """
        todos = self.prestamo_dao.read_all()
        if self.usuario_actual.rol == "estudiante":
            # Ver sólo sus préstamos
            prestamos = [p for p in todos if p.user_id == self.usuario_actual.user_id]
        else:
            # Admin ve todos
            prestamos = todos

        self.view.show_prestamos(prestamos)

    def crear_prestamo(self, libro_titulo: str):
        if not libro_titulo:
            self.view.mostrar_mensaje("Ingresa un título de libro.")
            return

        # 1) Verificar que el rol sea "estudiante" (si es requisito).
        if self.usuario_actual.rol != "estudiante":
            self.view.mostrar_mensaje("Solo un estudiante puede crear préstamos.")
            return

        # 2) Buscar el libro
        libro_encontrado = self.libro_dao.read_by_titulo(libro_titulo)
        if not libro_encontrado:
            self.view.mostrar_mensaje(f"No existe el libro '{libro_titulo}' en la base de datos.")
            return

        # 3) Verificar que estado == "DISPONIBLE"
        if libro_encontrado.estado != "DISPONIBLE":
            self.view.mostrar_mensaje(f"El libro '{libro_titulo}' no está disponible.")
            return

        # 4) Crear el préstamo
        nuevo_id = str(uuid.uuid4())
        nuevo_prestamo = Prestamo(
            prestamo_id=nuevo_id,
            user_id=self.usuario_actual.user_id,
            libro_titulo=libro_titulo,
            fecha_inicio=str(date.today()),
            fecha_fin=None,
            estado="ACTIVO"
        )

        exito_prestamo = self.prestamo_dao.create(nuevo_prestamo)
        if not exito_prestamo:
            self.view.mostrar_mensaje("Error al crear el préstamo.")
            return

        # 5) Actualizar el estado del libro a "No disponible"
        exito_libro = self.libro_dao.update_estado(libro_titulo, "NO DISPONIBLE")
        if not exito_libro:
            self.view.mostrar_mensaje("El préstamo se creó, pero no se pudo actualizar el estado del libro.")
            return

        self.view.mostrar_mensaje(f"Préstamo creado. Ahora el libro '{libro_titulo}' está No disponible.")
        
        # (Opcional) Recargar la lista de préstamos en la vista
        self.load_prestamos()
