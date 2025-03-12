from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class LibroView(QWidget):
    def __init__(self, libro_controller):
        super().__init__()
        self.libro_controller = libro_controller
        self.setWindowTitle("Ver Libros")
        self.setGeometry(470, 470, 500, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Al iniciar, podrías mostrar un texto vacío o un "Cargando..."
        self.info_label = QLabel("Lista de Libros:")
        self.layout.addWidget(self.info_label)

    def show_books(self, libros):
        """
        Recibe una lista de objetos Libro y los despliega en la ventana.
        """
        # Limpia el layout (opcionalmente)
        while self.layout.count() > 1:
            item = self.layout.takeAt(1)  # Deja el primer label en su lugar
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Ahora crea un QLabel por cada libro
        for libro in libros:
            label = QLabel(f"Título: {libro.titulo} | Autor: {libro.autor} | Género: {libro.genero} | Estado: {libro.estado}")
            self.layout.addWidget(label)

