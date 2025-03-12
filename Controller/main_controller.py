from View.libro_view import LibroView
from Controller.libro_controller import LibroController
from View.prestamo_view import PrestamoView
from Controller.prestamo_controller import PrestamoController

class MainController:
    def __init__(self, usuario_actual):
        self.usuario_actual = usuario_actual
        self.main_window = None

    def abrir_libros(self):
        libro_controller = LibroController(None)
        libro_view = LibroView(libro_controller)
        libro_view.show()

    def abrir_prestamos(self):
        prestamo_controller = PrestamoController(None)
        prestamo_view = PrestamoView(prestamo_controller)
        prestamo_view.show()
