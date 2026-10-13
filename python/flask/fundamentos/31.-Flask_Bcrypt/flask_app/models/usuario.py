import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(
    r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
)

class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validar_usuario(info):
        es_valido = True

        if not info["nombre"].strip():
            flash("El nombre es obligatorio.", "nombre")
            es_valido = False

        elif len(info["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "nombre")
            es_valido = False

        if not info["apellido"].strip():
            flash("El apellido es obligatorio.", "apellido")
            es_valido = False

        elif len(info["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "apellido")
            es_valido = False

        if not info["email"].strip():
            flash("El email es obligatorio.", "email")
            es_valido = False

        elif not EMAIL_REGEX.match(info["email"].strip()):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False

        if not info["password"]:
            flash("La contraseña es obligatoria.", "password")
            es_valido = False

        elif len(info["password"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "password")
            es_valido = False

        return es_valido

    @classmethod
    def guardar(cls, info):
        query = """
            INSERT INTO usr_list
            (nombre, apellido, email, password)
            VALUES
            (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL("esquema_loginreg").query_db(query, info)

    @classmethod
    def buscar_por_email(cls, info):
        query = """
            SELECT *
            FROM usr_list
            WHERE email = %(email)s;
        """
        resultados = connectToMySQL("esquema_loginreg").query_db(query, info)

        if len(resultados) == 1:
            return cls(resultados[0])

        return False

    @classmethod
    def existe_email(cls, info):
        query = """
            SELECT id
            FROM usr_list
            WHERE email = %(email)s;
        """
        resultados = connectToMySQL("esquema_loginreg").query_db(query, info)
        return len(resultados) > 0
