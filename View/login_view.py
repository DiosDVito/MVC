from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginView(QWidget):
    def __init__(self, login_controller):
        super().__init__()
        self.login_controller = login_controller

        self.setWindowTitle("Login")
        self.setGeometry(470, 470, 500, 400)

        layout = QVBoxLayout()

        self.labelEmail = QLabel("Email:")
        self.inputEmail = QLineEdit()
        layout.addWidget(self.labelEmail)
        layout.addWidget(self.inputEmail)

        self.labelPassword = QLabel("Contraseña:")
        self.inputPassword = QLineEdit()
        self.inputPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelPassword)
        layout.addWidget(self.inputPassword)

        self.btnIniciar = QPushButton("Iniciar Sesión")
        self.btnIniciar.clicked.connect(self.login_controller.do_login)
        layout.addWidget(self.btnIniciar)

        self.setLayout(layout)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, "Información", mensaje)
