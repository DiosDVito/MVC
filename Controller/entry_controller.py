from View.login_view import LoginView
from Controller.login_controller import LoginController

from View.register_view import RegisterView
from Controller.register_controller import RegisterController

class EntryController:
    def __init__(self):
        self.view = None

    def set_view(self, view):
        self.view = view

    def open_login(self):
        self.view.close()
        login_controller = LoginController()
        login_view = LoginView(login_controller)
        login_controller.set_view(login_view)
        login_view.show()

    def open_register(self):
        self.view.close()
        reg_controller = RegisterController()
        reg_view = RegisterView(reg_controller)
        reg_controller.set_view(reg_view)
        reg_view.show()
