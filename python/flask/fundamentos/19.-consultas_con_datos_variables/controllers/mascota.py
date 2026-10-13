



from connections.mysqlconnection import connectToMySQL






class Mascota:
    """
    Representa un record de la tabla mascotas.
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


    
    
    

    @classmethod
    def get_all(cls):
        """
        Devuelve todas las mascotas de la base de info.
        """

        query = """
            SELECT *
            FROM mascotas;
        """


        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)


        mascotas = []


        for mascota in resultados:

            mascotas.append(
                cls(mascota)
            )


        return mascotas


    
    
    

    @classmethod
    def get_by_id(cls, id):
        """
        Busca una mascota utilizando su ID.

        El ID recibido desde Python se envía como parámetro
        de una sentencia preparada.
        """

        
        
        

        query = """
            SELECT *
            FROM mascotas
            WHERE id = %(id_mascota)s;
        """


        
        
        

        data = {
            "id_mascota": id
        }


        
        
        

        resultados = connectToMySQL(
            "primera_flask"
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
    def get_by_tipo(cls, tipo):
        query = "SELECT * FROM mascotas WHERE tipo = %(tipo_mascota)s;"
        data = {"tipo_mascota": tipo}
        resultados = connectToMySQL("primera_flask").query_db(query, data)
        mascotas = []
        if resultados:
            for mascota in resultados:
                mascotas.append(cls(mascota))
        return mascotas
