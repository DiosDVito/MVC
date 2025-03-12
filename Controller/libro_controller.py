from Model.DAO.libro_dao import LibroDAO

class LibroController:
    def __init__(self):
        self.view = None
        self.libro_dao = LibroDAO()

    def set_view(self, view):
        self.view = view

    def load_books(self):
        """
        Llama al DAO para obtener todos los libros y se los pasa a la vista.
        """
        libros = self.libro_dao.read_all()
        self.view.show_books(libros)
