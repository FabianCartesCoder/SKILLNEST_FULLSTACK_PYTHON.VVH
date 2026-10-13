from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    """
    Representa un record de la tabla usr_list.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.contrasena = data["contrasena"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favoritos = []

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los usr_list.
        """

        query = """
            SELECT
                id,
                nombre,
                email,
                contrasena,
                created_at,
                updated_at
            FROM usr_list
            ORDER BY id;
        """

        resultados = connectToMySQL(
            "esquema_canciones"
        ).query_db(query)

        usr_list = []

        for usr_data in resultados:
            usr_list.append(cls(usr_data))

        return usr_list

    @classmethod
    def get_by_id(cls, id):
        """
        Obtiene un usr_data específico.
        """

        query = """
            SELECT
                id,
                nombre,
                email,
                contrasena,
                created_at,
                updated_at
            FROM usr_list
            WHERE id = %(id)s;
        """

        data = {
            "id": id
        }

        resultados = connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

        if resultados:
            return cls(resultados[0])

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
                email,
                contrasena
            )
            VALUES
            (
                %(nombre)s,
                %(email)s,
                %(contrasena)s
            );
        """

        return connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

    @classmethod
    def get_by_id_with_favorites(cls, data):
        """
        Obtiene un usr_data y todas las canciones
        que tiene marcadas como favoritas.
        """

        query = """
            SELECT
                usr_list.id AS usuario_id,
                usr_list.nombre AS usuario_nombre,
                usr_list.email AS usuario_email,
                usr_list.contrasena AS usuario_contrasena,
                usr_list.created_at AS usuario_created_at,
                usr_list.updated_at AS usuario_updated_at,

                canciones.id AS cancion_id,
                canciones.titulo AS cancion_titulo,
                canciones.artista AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at

            FROM usr_list

            LEFT JOIN favoritos
                ON favoritos.usuario_id = usr_list.id

            LEFT JOIN canciones
                ON favoritos.cancion_id = canciones.id

            WHERE usr_list.id = %(id)s;
        """

        resultados = connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

        if not resultados:
            return None

        usuario_data = {
            "id": resultados[0]["usuario_id"],
            "nombre": resultados[0]["usuario_nombre"],
            "email": resultados[0]["usuario_email"],
            "contrasena": resultados[0]["usuario_contrasena"],
            "created_at": resultados[0]["usuario_created_at"],
            "updated_at": resultados[0]["usuario_updated_at"]
        }

        usr_data = cls(usuario_data)

        for fila in resultados:

            if fila["cancion_id"] is not None:

                usr_data.favoritos.append({
                    "id": fila["cancion_id"],
                    "titulo": fila["cancion_titulo"],
                    "artista": fila["cancion_artista"],
                    "created_at": fila["cancion_created_at"],
                    "updated_at": fila["cancion_updated_at"]
                })

        return usr_data