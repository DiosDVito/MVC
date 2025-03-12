from Model.DAO.usuario_dao import UsuarioDAO
from Model.Objects.administrador import Administrador
from Model.Objects.estudiante import Estudiante
from Model.Objects.profesor import Profesor

class UsuarioController:
    def __init__(self, usuario_view):
        self.usuario_view = usuario_view
        self.usuario_dao = UsuarioDAO()

    def registrar_usuario(self):
        nombre = self.usuario_view.inputNombre.text().strip()
        email = self.usuario_view.inputEmail.text().strip()
        password = self.usuario_view.inputPassword.text().strip()
        rol = self.usuario_view.comboRol.currentText().lower()

        if not nombre or not email or not password:
            self.usuario_view.mostrar_mensaje("Por favor, completa todos los campos.")
            return

        # Dependiendo del rol, crea la instancia
        if rol == "administrador":
            usuario = Administrador(None, nombre, email)
        elif rol == "estudiante":
            usuario = Estudiante(None, nombre, email)
        elif rol == "profesor":
            usuario = Profesor(None, nombre, email)
        else:
            self.usuario_view.mostrar_mensaje("Rol inválido.")
            return

        # Insertar en Firestore (con ID automático)
        user_id_generado = self.usuario_dao.create_sin_id(usuario, password)
        if user_id_generado:
            self.usuario_view.mostrar_mensaje(f"Usuario '{nombre}' creado. ID={user_id_generado}")
            
            # Aquí decides si tras registrar:
            # - Cierras esta ventana y vuelves al login, o
            # - Directamente vas a la main window
            self.usuario_view.close()
            # Por ejemplo, podrías re-abrir login:
            # from view.login_view import LoginView
            # from controller.login_controller import LoginController
            # login_ctrl = LoginController(self.app_manager)
            # login_view = LoginView(login_ctrl)
            # login_view.show()
        else:
            self.usuario_view.mostrar_mensaje("Error al crear el usuario.")
