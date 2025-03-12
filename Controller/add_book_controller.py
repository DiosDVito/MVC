from Model.DAO.libro_dao import LibroDAO
from Model.Objects.libro import Libro

class AddBookController:
    def __init__(self):
        self.view = None
        self.libro_dao = LibroDAO()

    def set_view(self, view):
        self.view = view

    def guardar_libro(self):
        titulo = self.view.inputTitulo.text().strip()
        autor = self.view.inputAutor.text().strip()
        genero = self.view.inputGenero.text().strip()

        if not titulo or not autor or not genero:
            self.view.mostrar_mensaje("Todos los campos son obligatorios.")
            return

        nuevo_libro = Libro(titulo=titulo, autor=autor, genero=genero, estado="DISPONIBLE")
        exito = self.libro_dao.create(nuevo_libro)
        if exito:
            self.view.mostrar_mensaje(f"Libro '{titulo}' agregado con éxito.")
            self.view.close()  # Cierra la ventana de “Agregar Libro”
        else:
            self.view.mostrar_mensaje("Error al guardar el libro.")
