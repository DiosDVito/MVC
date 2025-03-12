from Model.Objects.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, user_id, nombre, email):
        super().__init__(user_id, nombre, email, "administrador")
