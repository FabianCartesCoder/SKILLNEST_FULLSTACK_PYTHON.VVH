# ==========================================================
# MODELO MASCOTA
# ==========================================================
from mysqlconnection import connectToMySQL

# ==========================================================
# CLASE MASCOTA
# ==========================================================
class Mascota:
    """
    Representa un registro de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Convierte un diccionario de MySQL en un objeto Mascota.
        """
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo = data["tipo"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ======================================================
    # OBTENER TODAS LAS MASCOTAS
    # ======================================================
    @classmethod
    def get_all(cls):
        """
        Devuelve todas las mascotas de la base de datos.
        """
        query = """
            SELECT *
            FROM mascotas;
        """

        resultados = connectToMySQL("primera_flask").query_db(query)
        mascotas = []

        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas

    # ======================================================
    # OBTENER MASCOTA POR ID
    # ======================================================
    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota utilizando su ID.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """

        data = {
            "id_mascota": id
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None

    # ======================================================
    # ACTIVIDAD: OBTENER MASCOTA POR NOMBRE
    # ======================================================
    @classmethod
    def get_by_name(cls, nombre):
        """
        Busca una mascota por su nombre exacto.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE nombre = %(nombre_mascota)s;
        """

        data = {
            "nombre_mascota": nombre
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None

    # ======================================================
    # DESAFÍO: OBTENER MASCOTAS POR TIPO
    # ======================================================
    @classmethod
    def get_by_tipo(cls, tipo):
        """
        Devuelve una lista de objetos Mascota según el tipo especificado.
        """
        query = """
            SELECT *
            FROM mascotas
            WHERE tipo = %(tipo_mascota)s;
        """

        data = {
            "tipo_mascota": tipo
        }

        resultados = connectToMySQL("primera_flask").query_db(query, data)
        mascotas = []

        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))

        return mascotas