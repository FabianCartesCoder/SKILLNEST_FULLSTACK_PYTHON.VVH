



from connection.mysqlconnection import connectToMySQL






class Mascota:
    """
    Representa un record de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en un objeto Mascota.
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
        Recupera todas las mascotas de la base de info.
        """

        query = """
            SELECT
                id,
                nombre,
                tipo,
                color,
                created_at,
                updated_at
            FROM mascotas
            ORDER BY id;
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
    def save(cls, info):
        """
        Crea una nueva mascota en la base de info.

        Recibe un diccionario llamado "info" con:

        nombre
        tipo
        color
        """

        
        
        
        
        
        
        
        
        

        query = """
            INSERT INTO mascotas
            (
                nombre,
                tipo,
                color,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(tipo)s,
                %(color)s,
                NOW(),
                NOW()
            );
        """


        
        
        

        return connectToMySQL(
            "primera_flask"
        ).query_db(
            query,
            info
        )
