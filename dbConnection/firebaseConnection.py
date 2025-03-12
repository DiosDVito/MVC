import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

_db_client = None

def get_firestore_client():
    """
    Retorna una única instancia del cliente Firestore.
    """
    global _db_client
    if _db_client is None:
        load_dotenv()  # Carga variables de entorno
        cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

        if not firebase_admin._apps:  # Si no hay app inicializada
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)

        _db_client = firestore.client()
    return _db_client
