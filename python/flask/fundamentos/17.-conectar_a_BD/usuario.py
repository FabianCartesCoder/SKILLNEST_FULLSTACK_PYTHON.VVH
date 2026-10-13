from mysqlconnection import connectToMySQL
class Usuario:
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.email = data["email"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usr_list;"
        resultados = connectToMySQL(
            "primera_flask"
        ).query_db(query)
        usr_list = []
        for usr_data in resultados:
            usr_list.append(
                cls(usr_data)
            )
        return usr_list