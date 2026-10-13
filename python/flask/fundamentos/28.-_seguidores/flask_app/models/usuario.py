from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    """
    Representa un record de la tabla usr_list.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los usr_list.
        """

        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usr_list
            ORDER BY nombre, apellido;
        """

        resultados = connectToMySQL(
            "esquema_seguidores"
        ).query_db(query)

        usr_list = []

        for usr_data in resultados:
            usr_list.append(
                cls(usr_data)
            )

        return usr_list

    @classmethod
    def get_by_id(cls, id):
        """
        Obtiene un usr_data específico mediante su ID.
        """

        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usr_list
            WHERE id = %(id)s;
        """

        data = {
            "id": id
        }

        res = connectToMySQL(
            "esquema_seguidores"
        ).query_db(
            query,
            data
        )

        if res:
            return cls(res[0])

        return None

    @classmethod
    def save(cls, data):
        """
        Crea un nuevo usr_data.
        """

        query = """
            INSERT INTO usr_list
            (
                nombre,
                apellido,
                email
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s
            );
        """

        return connectToMySQL(
            "esquema_seguidores"
        ).query_db(
            query,
            data
        )