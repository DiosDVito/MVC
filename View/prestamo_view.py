from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)

class PrestamoView(QWidget):
    def __init__(self, prestamo_controller):
        super().__init__()
        self.prestamo_controller = prestamo_controller
        self.setWindowTitle("Gestión de Préstamos")
        self.setGeometry(470, 470, 500, 400)

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # ----------------------------------------------------------------
        # SECCIÓN A) Formulario para que el ESTUDIANTE pida un nuevo préstamo
        # ----------------------------------------------------------------
        if self.prestamo_controller.usuario_actual.rol == "estudiante":
            self.info_label = QLabel("Pedir un nuevo préstamo:")
            self.lblLibro = QLabel("Título del libro:")
            self.txtLibro = QLineEdit()
            self.btnConfirmar = QPushButton("Confirmar Préstamo")
            self.btnConfirmar.clicked.connect(self.confirmar_prestamo)

            self.main_layout.addWidget(self.info_label)
            self.main_layout.addWidget(self.lblLibro)
            self.main_layout.addWidget(self.txtLibro)
            self.main_layout.addWidget(self.btnConfirmar)

        # ----------------------------------------------------------------
        # SECCIÓN B) Título para la lista de préstamos
        # (aparece para todos, pero el texto puede personalizarse)
        # ----------------------------------------------------------------
        if self.prestamo_controller.usuario_actual.rol == "estudiante":
            self.lblLista = QLabel("Tus Préstamos:")
        else:
            self.lblLista = QLabel("Lista de TODOS los Préstamos:")

        self.main_layout.addWidget(self.lblLista)

        # ----------------------------------------------------------------
        # SECCIÓN C) Sub-layout para la lista de préstamos
        # ----------------------------------------------------------------
        self.lista_layout = QVBoxLayout()
        self.main_layout.addLayout(self.lista_layout)

    def confirmar_prestamo(self):
        """
        Llamado cuando el estudiante hace clic en "Confirmar Préstamo".
        Toma el texto de self.txtLibro y llama al controlador.
        """
        libro = self.txtLibro.text().strip()
        self.prestamo_controller.crear_prestamo(libro)

    def show_prestamos(self, prestamos):
        """
        Muestra la lista de préstamos en la ventana, usando el sub-layout 'lista_layout'.
        """
        # 1) Limpia todo lo que hubiera en lista_layout
        while self.lista_layout.count():
            item = self.lista_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # 2) Crea un QLabel por cada préstamo
        for p in prestamos:
            label = QLabel(
                f"Libro: {p.libro_titulo} | Estado: {p.estado}"
            )
            self.lista_layout.addWidget(label)

    def mostrar_mensaje(self, mensaje):
        """
        Muestra un diálogo emergente con el mensaje.
        """
        QMessageBox.information(self, "Información", mensaje)
