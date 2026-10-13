from flask_app.config.mysqlconnection import connectToMySQL


class Favorito:
    """
    Representa una relación entre un usr_data y una canción.
    """

    @classmethod
    def existe(cls, data):
        """
        Comprueba si la relación ya existe.
        """

        query = """
            SELECT
                usuario_id,
                cancion_id
            FROM favoritos
            WHERE usuario_id = %(usuario_id)s
              AND cancion_id = %(cancion_id)s;
        """

        res = connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)

        return bool(res)

    @classmethod
    def agregar(cls, data):
        """
        Agrega una canción a los favoritos
        de un usr_data.
        """

        query = """
            INSERT INTO favoritos
            (
                usuario_id,
                cancion_id
            )
            VALUES
            (
                %(usuario_id)s,
                %(cancion_id)s
            );
        """

        return connectToMySQL(
            "esquema_canciones"
        ).query_db(query, data)