



from connection.mysqlconnection import connectToMySQL






class Usuario:
    """
    Representa un record de la tabla usr_list.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en un objeto Usuario.
        """

        self.id = data["id"]

        self.nombre = data["nombre"]

        self.apellido = data["apellido"]

        self.email = data["email"]

        self.created_at = data["created_at"]

        self.updated_at = data["updated_at"]


    
    
    
    

    @classmethod
    def get_all(cls):
        """
        Recupera todos los usr_list.
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
            ORDER BY id;
        """


        resultados = connectToMySQL(
            "esquema_usuarios"
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
        Busca un usr_data específico mediante su ID.

        Si existe:
            devuelve un objeto Usuario.

        Si no existe:
            devuelve None.
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


        resultados = connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )


        if resultados:

            return cls(
                resultados[0]
            )


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
                email,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s,
                NOW(),
                NOW()
            );
        """


        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )


    
    
    
    

    @classmethod
    def update(cls, data):
        """
        Actualiza los info de un usr_data existente.

        data debe contener:

        id
        nombre
        apellido
        email
        """

        query = """
            UPDATE usr_list
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """


        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )


    
    
    
    

    @classmethod
    def delete(cls, id):
        """
        Elimina un usr_data utilizando su ID.
        """

        query = """
            DELETE FROM usr_list
            WHERE id = %(id)s;
        """


        data = {
            "id": id
        }


        return connectToMySQL(
            "esquema_usuarios"
        ).query_db(
            query,
            data
        )