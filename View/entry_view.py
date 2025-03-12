from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class EntryView(QWidget):
    def __init__(self, entry_controller):
        super().__init__()
        self.entry_controller = entry_controller

        self.setWindowTitle("Bienvenido a la Biblioteca")
        self.setGeometry(470, 470, 500, 400)
        layout = QVBoxLayout()

        self.label = QLabel("¿Qué deseas hacer?")
        layout.addWidget(self.label)

        self.btnLogin = QPushButton("Iniciar Sesión")
        self.btnLogin.clicked.connect(self.entry_controller.open_login)
        layout.addWidget(self.btnLogin)

        self.btnRegister = QPushButton("Registrarse")
        self.btnRegister.clicked.connect(self.entry_controller.open_register)
        layout.addWidget(self.btnRegister)

        self.setLayout(layout)
