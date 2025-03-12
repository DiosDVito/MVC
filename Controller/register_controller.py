# controller/register_controller.py

from Model.DAO.usuario_dao import UsuarioDAO
from Model.Objects.administrador import Administrador
from Model.Objects.estudiante import Estudiante
from Model.Objects.profesor import Profesor
from Model.Objects.usuario import Usuario

from View.main_window import MainWindow
from Controller.main_window_controller import MainWindowController

class RegisterController:
    def __init__(self):
        self.view = None
        self.usuario_dao = UsuarioDAO()

    def set_view(self, view):
        self.view = view

    def do_register(self):
        nombre = self.view.inputNombre.text().strip()
        email = self.view.inputEmail.text().strip()
        password = self.view.inputPassword.text().strip()
        rol = self.view.comboRol.currentText().lower()

        if not nombre or not email or not password:
            self.view.mostrar_mensaje("Todos los campos son obligatorios.")
            return

        # Crear instancia base (sin ID)
        if rol == "administrador":
            usuario = Administrador(None, nombre, email)
        elif rol == "estudiante":
            usuario = Estudiante(None, nombre, email)
        elif rol == "profesor":
            usuario = Profesor(None, nombre, email)
        else:
            usuario = Usuario(None, nombre, email, rol)

        user_id = self.usuario_dao.create_sin_id(usuario, password)
        if user_id:
            self.view.mostrar_mensaje(f"Usuario '{nombre}' registrado. ID = {user_id}")
            # Cerrar la ventana de registro
            self.view.close()

            # Abrir MainWindow
            mw_controller = MainWindowController()
            mw_view = MainWindow(mw_controller)
            mw_controller.set_view(mw_view)
            mw_view.show()
        else:
            self.view.mostrar_mensaje("Error al crear el usuario.")
