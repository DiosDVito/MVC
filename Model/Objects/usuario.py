class Usuario:
    def __init__(self, user_id, nombre, email, rol):
        self.user_id = user_id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.nombre} <{self.email}> (Rol: {self.rol})"
