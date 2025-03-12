from Model.Objects.libro import Libro
from dbConnection.firebaseConnection import get_firestore_client

class LibroDAO:
    def __init__(self):
        self.db = get_firestore_client()

    def read_by_titulo(self, titulo: str):
        """
        Retorna un objeto Libro si existe un documento con el título dado,
        de lo contrario retorna None.
        """
        doc_ref = self.db.collection("libros").document(titulo)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return Libro(
                titulo=data.get("titulo"),
                autor=data.get("autor"),
                genero=data.get("genero"),
                estado=data.get("estado", "DISPONIBLE")
            )
        return None
    
    def create(self, libro: Libro):
        try:
            doc_ref = self.db.collection("libros").document(libro.titulo)
            doc_ref.set({
                "titulo": libro.titulo,
                "autor": libro.autor,
                "genero": libro.genero,
                "estado": libro.estado
            })
            return True
        except Exception as e:
            print(f"Error creando libro: {e}")
            return False

    def read_all(self):
        libros = []
        try:
            docs = self.db.collection("libros").stream()
            for doc in docs:
                data = doc.to_dict()
                libros.append(
                    Libro(
                        titulo=data.get("titulo"),
                        autor=data.get("autor"),
                        genero=data.get("genero"),
                        estado=data.get("estado", "DISPONIBLE")
                    )
                )
        except Exception as e:
            print(f"Error leyendo libros: {e}")
        return libros


    def update_estado(self, titulo, nuevo_estado):
        try:
            doc_ref = self.db.collection("libros").document(titulo)
            doc_ref.update({"estado": nuevo_estado})
            return True
        except Exception as e:
            print(f"Error actualizando estado del libro: {e}")
            return False


    def delete(self, titulo):
        try:
            doc_ref = self.db.collection("libros").document(titulo)
            doc_ref.delete()
            return True
        except Exception as e:
            print(f"Error eliminando libro: {e}")
            return False
