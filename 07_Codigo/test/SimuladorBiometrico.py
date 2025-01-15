import cv2
from pymongo import MongoClient
import numpy as np

class BiometricSimulator:
    def __init__(self, db_name='biometric_db'):
        # Inicializar conexión a MongoDB
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db['users']
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def is_username_taken(self, username):
        """Verifica si el nombre de usuario ya está registrado."""
        return self.collection.find_one({'username': username}) is not None

    def register_user(self, username, password):
        """Registra un nuevo usuario."""
        if self.is_username_taken(username):
            print(f"Usuario '{username}' ya está registrado.")
            return "Error: El nombre de usuario ya está en uso."
        
        user_data = {
            'username': username,
            'password': password,
            'face_data': []  # Almacena datos de rostro
        }
        try:
            result = self.collection.insert_one(user_data)
            print(f"Usuario '{username}' registrado con ID: {result.inserted_id}")
            return f"Usuario {username} registrado con éxito."
        except Exception as e:
            print("Error al insertar en la base de datos:", e)
            return "Error: No se pudo registrar el usuario."

    def capture_face(self, username):
        """Captura y almacena la imagen facial del usuario."""
        if not self.is_username_taken(username):
            return "Error: El usuario no está registrado."

        # Simular captura de datos faciales
        try:
            fake_face_data = [[1, 2, 3], [4, 5, 6]]  # Simulación de datos de rostro
            result = self.collection.update_one(
                {'username': username},
                {'$set': {'face_data': fake_face_data}}
            )
            if result.modified_count > 0:
                print(f"Datos faciales del usuario '{username}' actualizados exitosamente.")
                return f"Datos faciales del usuario {username} guardados con éxito."
            else:
                return "Error: No se pudieron actualizar los datos faciales."
        except Exception as e:
            print("Error al actualizar los datos faciales:", e)
            return "Error: No se pudieron guardar los datos faciales."

    def verify_face(self, username):
        """Verifica la identidad del usuario con reconocimiento facial."""
        user_data = self.collection.find_one({'username': username})
        if not user_data:
            return "Error: Usuario no encontrado."

        if not user_data['face_data']:
            return "Error: No hay datos faciales almacenados para este usuario."

        # Simular verificación facial
        return "Verificación fallida. Rostro no reconocido."

    def verify_user(self, username, password):
        """Verifica el usuario y la contraseña."""
        user_data = self.collection.find_one({'username': username})
        if user_data and user_data['password'] == password:
            return f"¡Bienvenido, {username}!"
        return "Error: Credenciales incorrectas."
