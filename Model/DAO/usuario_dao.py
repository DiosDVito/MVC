from dbConnection.firebaseConnection import get_firestore_client
from Model.Objects.administrador import Administrador
from Model.Objects.estudiante import Estudiante
from Model.Objects.profesor import Profesor
from Model.Objects.usuario import Usuario

import uuid

class UsuarioDAO:
    def __init__(self):
        self.db = get_firestore_client()

    def create_sin_id(self, usuario: Usuario, password: str):
        """
        Crea un documento en la colección 'usuarios' y deja que Firestore genere un ID.
        Guarda también la contraseña en texto plano (solo demo).
        Retorna el ID generado.
        """
        try:
            data = {
                "nombre": usuario.nombre,
                "email": usuario.email,
                "rol": usuario.rol,
                "password": password
            }
            doc_ref = self.db.collection("usuarios").document()
            auto_id = doc_ref.id

            data["user_id"] = auto_id
            doc_ref.set(data)

            return auto_id
        except Exception as e:
            print(f"Error creando usuario: {e}")
            return None

    def read_by_email_and_password(self, email: str, password: str):
        """
        Retorna un dict con los datos del usuario si coincide email+password.
        De lo contrario, None.
        """
        try:
            ref = self.db.collection("usuarios")
            query = ref.where("email", "==", email).where("password", "==", password).stream()
            for doc in query:
                return doc.to_dict()  # Retorna el primer match
            return None
        except Exception as e:
            print(f"Error autenticando usuario: {e}")
            return None

    def read_by_id(self, user_id: str):
        """
        Retorna una instancia de Usuario (Administrador, Estudiante, Profesor) según rol.
        """
        try:
            doc_ref = self.db.collection("usuarios").document(user_id)
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict()
                rol = data["rol"]
                if rol == "administrador":
                    return Administrador(data["user_id"], data["nombre"], data["email"])
                elif rol == "estudiante":
                    return Estudiante(data["user_id"], data["nombre"], data["email"])
                elif rol == "profesor":
                    return Profesor(data["user_id"], data["nombre"], data["email"])
                else:
                    return Usuario(data["user_id"], data["nombre"], data["email"], rol)
            return None
        except Exception as e:
            print(f"Error leyendo usuario por ID: {e}")
            return None
