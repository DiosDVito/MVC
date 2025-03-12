from dbConnection.firebaseConnection import get_firestore_client
from Model.Objects.prestamo import Prestamo

class PrestamoDAO:
    def __init__(self):
        self.db = get_firestore_client()

    def create(self, prestamo: Prestamo):
        try:
            doc_ref = self.db.collection("prestamos").document(prestamo.prestamo_id)
            doc_ref.set({
                "prestamo_id": prestamo.prestamo_id,
                "user_id": prestamo.user_id,
                "user_name": prestamo.user_name,
                "libro_titulo": prestamo.libro_titulo,
                "fecha_inicio": prestamo.fecha_inicio,
                "fecha_fin": prestamo.fecha_fin,
                "estado": prestamo.estado
            })
            return True
        except Exception as e:
            print(f"Error creando préstamo: {e}")
            return False

    def read_all(self):
        prestamos = []
        try:
            docs = self.db.collection("prestamos").stream()
            for doc in docs:
                data = doc.to_dict()
                prestamos.append(
                    Prestamo(
                        prestamo_id  = data.get("prestamo_id"),
                        user_id      = data.get("user_id"),
                        user_name    = data.get("user_name"),
                        libro_titulo = data.get("libro_titulo"),
                        fecha_inicio = data.get("fecha_inicio"),
                        fecha_fin    = data.get("fecha_fin"),
                        estado       = data.get("estado", "ACTIVO")
                    )
                )
        except Exception as e:
            print(f"Error leyendo prestamos: {e}")
        return prestamos

    def update_estado(self, prestamo_id, nuevo_estado):
        try:
            doc_ref = self.db.collection("prestamos").document(prestamo_id)
            doc_ref.update({"estado": nuevo_estado})
            return True
        except Exception as e:
            print(f"Error actualizando préstamo: {e}")
            return False

    def delete(self, prestamo_id):
        try:
            doc_ref = self.db.collection("prestamos").document(prestamo_id)
            doc_ref.delete()
            return True
        except Exception as e:
            print(f"Error eliminando préstamo: {e}")
            return False
