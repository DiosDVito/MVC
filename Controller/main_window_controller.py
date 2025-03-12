from Controller.libro_controller import LibroController
from View.libro_view import LibroView
from Controller.prestamo_controller import PrestamoController
from View.prestamo_view import PrestamoView

class MainWindowController:
    def __init__(self, usuario_actual):
        self.view = None
        self.usuario_actual = usuario_actual

    def set_view(self, view):
        self.view = view

    def open_libros(self):
        from Controller.libro_controller import LibroController
        from View.libro_view import LibroView

        lb_controller = LibroController()
        lb_view = LibroView(lb_controller)
        lb_controller.set_view(lb_view)

        # Cargar la lista de libros antes o después de show():
        lb_controller.load_books()

        lb_view.show()

    # main_window_controller.py (o similar)
    def open_prestamo(self):
        from Controller.prestamo_controller import PrestamoController
        from View.prestamo_view import PrestamoView

        pr_controller = PrestamoController(self.usuario_actual) 
        pr_view = PrestamoView(pr_controller)
        pr_controller.set_view(pr_view)

        # Cargar la lista de préstamos (todos o los del estudiante)
        pr_controller.load_prestamos()

        pr_view.show()

    
    def agregar_libro(self):
        """
        Abre la ventana para agregar un nuevo libro.
        """
        # Crearemos un AddBookController + AddBookView (explicado más abajo)
        from Controller.add_book_controller import AddBookController
        from View.add_book_view import AddBookView

        add_book_ctrl = AddBookController()
        add_book_view = AddBookView(add_book_ctrl)
        add_book_ctrl.set_view(add_book_view)
        add_book_view.show()