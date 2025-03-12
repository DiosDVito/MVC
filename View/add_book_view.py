from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class AddBookView(QWidget):
    def __init__(self, add_book_controller):
        super().__init__()
        self.add_book_controller = add_book_controller

        self.setWindowTitle("Agregar Libro")
        self.setGeometry(470, 470, 500, 400)

        layout = QVBoxLayout()

        self.labelTitulo = QLabel("Título:")
        self.inputTitulo = QLineEdit()
        layout.addWidget(self.labelTitulo)
        layout.addWidget(self.inputTitulo)

        self.labelAutor = QLabel("Autor:")
        self.inputAutor = QLineEdit()
        layout.addWidget(self.labelAutor)
        layout.addWidget(self.inputAutor)

        self.labelGenero = QLabel("Género:")
        self.inputGenero = QLineEdit()
        layout.addWidget(self.labelGenero)
        layout.addWidget(self.inputGenero)

        self.btnGuardar = QPushButton("Guardar")
        self.btnGuardar.clicked.connect(self.add_book_controller.guardar_libro)
        layout.addWidget(self.btnGuardar)

        self.setLayout(layout)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, "Información", mensaje)
