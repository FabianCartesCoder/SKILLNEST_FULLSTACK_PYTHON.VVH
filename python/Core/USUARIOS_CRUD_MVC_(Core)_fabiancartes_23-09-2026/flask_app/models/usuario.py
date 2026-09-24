from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data.get("id")
        self.nombre = data.get("nombre")
        self.apellido = data.get("apellido")
        self.email = data.get("email")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM usuarios ORDER BY id DESC;"
        resultados = connectToMySQL("esquema_usuarios").query_db(query)
        return [cls(u) for u in resultados] if resultados else []

    @classmethod
    def obtener_por_id(cls, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        params = {"id": usuario_id}
        resultados = connectToMySQL("esquema_usuarios").query_db(query, params)
        return cls(resultados[0]) if resultados else None

    @classmethod
    def guardar(cls, formulario):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL("esquema_usuarios").query_db(query, formulario)

    @classmethod
    def actualizar(cls, formulario):
        query = """
            UPDATE usuarios 
            SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL("esquema_usuarios").query_db(query, formulario)

    @classmethod
    def eliminar(cls, usuario_id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL("esquema_usuarios").query_db(query, {"id": usuario_id})

    @staticmethod
    def validar_datos(datos):
        es_valido = True
        errores = []

        if len(datos.get("nombre", "").strip()) < 2:
            errores.append("El nombre debe tener al menos 2 caracteres.")
            es_valido = False

        if len(datos.get("apellido", "").strip()) < 2:
            errores.append("El apellido debe tener al menos 2 caracteres.")
            es_valido = False

        if not EMAIL_REGEX.match(datos.get("email", "").strip()):
            errores.append("Ingrese un correo electrónico válido.")
            es_valido = False

        return es_valido, errores