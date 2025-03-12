from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self, main_window_controller):
        super().__init__()
        self.main_window_controller = main_window_controller
        self.setWindowTitle("Menú Principal - Biblioteca")
        self.setGeometry(470, 470, 500, 400)

        layout = QVBoxLayout()

        self.label = QLabel(f"Bienvenido, {self.main_window_controller.usuario_actual.nombre}")
        layout.addWidget(self.label)

        self.btnLibros = QPushButton("Ver Libros")
        self.btnLibros.clicked.connect(self.main_window_controller.open_libros)
        layout.addWidget(self.btnLibros)

        if self.main_window_controller.usuario_actual.rol == "administrador":
            self.btnPrestamo = QPushButton("Ver Préstamos")
            self.btnPrestamo.clicked.connect(self.main_window_controller.open_prestamo)
            layout.addWidget(self.btnPrestamo)
        else:
            self.btnPrestamo = QPushButton("Pedir Préstamo")
            self.btnPrestamo.clicked.connect(self.main_window_controller.open_prestamo)
            layout.addWidget(self.btnPrestamo)

        # SOLO si el usuario es administrador, muestra "Agregar Libro"
        if self.main_window_controller.usuario_actual.rol == "administrador":
            self.btnAgregarLibro = QPushButton("Agregar Libro")
            self.btnAgregarLibro.clicked.connect(self.main_window_controller.agregar_libro)
            layout.addWidget(self.btnAgregarLibro)

        self.setLayout(layout)
