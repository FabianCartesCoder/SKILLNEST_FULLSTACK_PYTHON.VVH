



import pymysql.cursors






class MySQLConnection:
    """
    Administra una conexión con una base de info MySQL.
    """

    def __init__(self, db):
        """
        Establece una conexión con la base de info
        recibida como parámetro.
        """

        self.connection = pymysql.connect(

            host="localhost",

            user="root",

            password="1234",

            database="primera_flask",

            charset="utf8mb4",

            cursorclass=pymysql.cursors.DictCursor,

            autocommit=True

        )


    
    
    

    def query_db(self, query, data=None):
        """
        Ejecuta una query SQL.

        query:
            Cadena con la query SQL.

        data:
            Diccionario con los valores que serán enviados
            a los parámetros de la query.
        """

        with self.connection.cursor() as cursor:

            try:

                
                
                

                cursor.execute(query, data)


                
                
                

                if query.strip().lower().startswith("select"):

                    resultados = cursor.fetchall()

                    return resultados


                
                
                

                elif query.strip().lower().startswith("insert"):

                    return cursor.lastrowid


                
                
                

                else:

                    return None


            except Exception as e:

                print("Something went wrong:")

                print(e)

                return False


            finally:

                
                
                

                self.connection.close()






def connectToMySQL(db):
    """
    Crea y devuelve una instancia de MySQLConnection.
    """

    return MySQLConnection(db)