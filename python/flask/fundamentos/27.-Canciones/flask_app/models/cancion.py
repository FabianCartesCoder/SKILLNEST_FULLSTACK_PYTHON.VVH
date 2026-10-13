from flask_app.config.mysqlconnection import connectToMySQL


class Cancion:
    """
    Representa un record de la tabla canciones.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.titulo = data["titulo"]
        self.artista = data["artista"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.usr_list = []

    @classmethod
    def get_all(cls):
        """
        Obtiene todas las canciones.
        """

        query = """
            SELECT
                id,
                titulo,
                artista,
                created_at,
                updated_at
            FROM canciones
            ORDER BY id;
        """

        resultados = connectToMySQL(
            "esquema_canciones"
        ).query_db(query)

        canciones = []

        for cancion in resultados:
            canciones.append(cls(cancion))

        return canciones

    @classmethod
    def get_by_id(cls, id):
        """
        Obtiene una canción por su ID.
        """

        query = """
            SELECT
                id,
                titulo,
                artista,
                created_at,
                updated_at
            FROM canciones
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
        Crea una nueva canción.
        """

        query = """
            INSERT INTO canciones
            (
                titulo,
                artista
            )
            VALUES
            (
                %(titulo)s,
                %(artista)s
            );
        """

        return connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

    @classmethod
    def get_by_id_with_users(cls, data):
        """
        Obtiene una canción y todos los usr_list
        que la tienen como favorita.
        """

        query = """
            SELECT
                canciones.id AS cancion_id,
                canciones.titulo AS cancion_titulo,
                canciones.artista AS cancion_artista,
                canciones.created_at AS cancion_created_at,
                canciones.updated_at AS cancion_updated_at,

                usr_list.id AS usuario_id,
                usr_list.nombre AS usuario_nombre,
                usr_list.email AS usuario_email,
                usr_list.contrasena AS usuario_contrasena,
                usr_list.created_at AS usuario_created_at,
                usr_list.updated_at AS usuario_updated_at

            FROM canciones

            LEFT JOIN favoritos
                ON favoritos.cancion_id = canciones.id

            LEFT JOIN usr_list
                ON favoritos.usuario_id = usr_list.id

            WHERE canciones.id = %(id)s;
        """

        resultados = connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

        if not resultados:
            return None

        cancion_data = {
            "id": resultados[0]["cancion_id"],
            "titulo": resultados[0]["cancion_titulo"],
            "artista": resultados[0]["cancion_artista"],
            "created_at": resultados[0]["cancion_created_at"],
            "updated_at": resultados[0]["cancion_updated_at"]
        }

        cancion = cls(cancion_data)

        for fila in resultados:

            if fila["usuario_id"] is not None:

                cancion.usr_list.append({
                    "id": fila["usuario_id"],
                    "nombre": fila["usuario_nombre"],
                    "email": fila["usuario_email"],
                    "contrasena": fila["usuario_contrasena"],
                    "created_at": fila["usuario_created_at"],
                    "updated_at": fila["usuario_updated_at"]
                })

        return cancion

    @classmethod
    def get_users_not_favorited(cls, data):
        """
        Obtiene solamente los usr_list que todavía
        no han marcado la canción como favorita.
        """

        query = """
            SELECT
                usr_list.id,
                usr_list.nombre,
                usr_list.email,
                usr_list.contrasena,
                usr_list.created_at,
                usr_list.updated_at

            FROM usr_list

            LEFT JOIN favoritos
                ON favoritos.usuario_id = usr_list.id
                AND favoritos.cancion_id = %(cancion_id)s

            WHERE favoritos.usuario_id IS NULL

            ORDER BY usr_list.nombre;
        """

        return connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)