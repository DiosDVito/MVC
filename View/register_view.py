from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QMessageBox
)

class RegisterView(QWidget):
    def __init__(self, register_controller):
        super().__init__()
        self.register_controller = register_controller

        self.setWindowTitle("Registrar Usuario")
        self.setGeometry(470, 470, 500, 400)

        layout = QVBoxLayout()

        self.labelNombre = QLabel("Nombre:")
        self.inputNombre = QLineEdit()
        layout.addWidget(self.labelNombre)
        layout.addWidget(self.inputNombre)

        self.labelEmail = QLabel("Email:")
        self.inputEmail = QLineEdit()
        layout.addWidget(self.labelEmail)
        layout.addWidget(self.inputEmail)

        self.labelPassword = QLabel("Contraseña:")
        self.inputPassword = QLineEdit()
        self.inputPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.labelPassword)
        layout.addWidget(self.inputPassword)

        self.labelRol = QLabel("Rol:")
        self.comboRol = QComboBox()
        self.comboRol.addItems(["administrador", "estudiante", "profesor"])
        layout.addWidget(self.labelRol)
        layout.addWidget(self.comboRol)

        self.btnRegistrar = QPushButton("Registrar")
        self.btnRegistrar.clicked.connect(self.register_controller.do_register)
        layout.addWidget(self.btnRegistrar)

        self.setLayout(layout)

    def mostrar_mensaje(self, mensaje):
        QMessageBox.information(self, "Información", mensaje)
