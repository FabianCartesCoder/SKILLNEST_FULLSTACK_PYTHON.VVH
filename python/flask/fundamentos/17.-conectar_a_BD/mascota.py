from mysqlconnection import connectToMySQL
class Mascota:
    """
    Representa un record de la tabla mascotas.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y transforma sus info en atributos del objeto.
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
        Consulta todas las mascotas almacenadas
        en la base de info.

        Retorna una lista de objetos Mascota.
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
    def get_by_id(cls,id):
        query = "SELECT * FROM usr_list WHERE id = %(id)s"
        data = {
            "id": id
        }
        resultados = connectToMySQL("primera_flask").query_db(query,data)

        if resultados:
            return resultados
        return None
        
