from PyQt5.QtWidgets import QMessageBox
from Model.DAO.usuario_dao import UsuarioDAO

# Importamos las clases de usuario
from Model.Objects.administrador import Administrador
from Model.Objects.estudiante import Estudiante
from Model.Objects.profesor import Profesor
from Model.Objects.usuario import Usuario

# Importamos la MainWindow y su controlador
from View.main_window import MainWindow
from Controller.main_window_controller import MainWindowController

class LoginController:
    def __init__(self):
        self.view = None
        self.usuario_dao = UsuarioDAO()

    def set_view(self, view):
        """
        Método para establecer la referencia a la vista de login.
        Suele llamarse justo después de crear el LoginController y el LoginView.
        """
        self.view = view

    def do_login(self):
        """
        Método llamado cuando se hace clic en "Iniciar Sesión" en login_view.
        1. Lee email y password de la vista.
        2. Valida credenciales con el DAO (Firestore).
        3. Si coinciden, crea la instancia de usuario según el rol y abre la ventana principal.
        4. Si falla, muestra mensaje de error.
        """
        email = self.view.inputEmail.text().strip()
        password = self.view.inputPassword.text().strip()

        if not email or not password:
            self.view.mostrar_mensaje("Email y contraseña no pueden estar vacíos.")
            return

        # Consultar en Firebase si existe un usuario con ese email/password
        usuario_data = self.usuario_dao.read_by_email_and_password(email, password)

        if usuario_data:
            # Credenciales correctas, creamos la instancia de Usuario
            rol = usuario_data.get("rol")
            user_id = usuario_data.get("user_id")
            nombre = usuario_data.get("nombre")
            email_db = usuario_data.get("email")

            # Dependiendo del rol, instanciamos la subclase correspondiente
            if rol == "administrador":
                usuario_actual = Administrador(user_id, nombre, email_db)
            elif rol == "estudiante":
                usuario_actual = Estudiante(user_id, nombre, email_db)
            elif rol == "profesor":
                usuario_actual = Profesor(user_id, nombre, email_db)
            else:
                usuario_actual = Usuario(user_id, nombre, email_db, rol)

            # Cerrar la ventana de login
            self.view.close()

            # Crear la ventana principal y su controlador, pasándole el usuario
            main_window_controller = MainWindowController(usuario_actual)
            main_window = MainWindow(main_window_controller)
            main_window_controller.set_view(main_window)
            main_window.show()

        else:
            # No se encontró usuario o password incorrecto
            self.view.mostrar_mensaje("Credenciales inválidas. Intenta de nuevo.")
