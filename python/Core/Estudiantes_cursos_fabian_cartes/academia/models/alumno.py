from academia.config.conexion import connectToMySQL

BD = "academia_talleres"


class Alumno:
    """Representa un record de la tabla alumnos."""

    def __init__(self, info):
        self.id = info["id"]
        self.nombre = info["nombre"]
        self.apellido = info["apellido"]
        self.edad = info["edad"]
        self.created_at = info["created_at"]
        self.updated_at = info["updated_at"]
        self.taller_id = info["taller_id"]

    @classmethod
    def guardar(cls, info):
        """Crea un alumno asociado a un taller."""
        query = """
            INSERT INTO alumnos
                (nombre, apellido, edad, taller_id)
            VALUES
                (%(nombre)s, %(apellido)s, %(edad)s, %(taller_id)s);
        """
        return connectToMySQL(BD).query_db(query, info)
