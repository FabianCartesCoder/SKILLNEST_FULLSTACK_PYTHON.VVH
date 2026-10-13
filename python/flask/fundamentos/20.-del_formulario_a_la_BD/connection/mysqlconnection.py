



import pymysql.cursors






class MySQLConnection:
    """
    Administra la conexión entre Python y MySQL.
    """

    def __init__(self, db):
        """
        Recibe el nombre de la base de info
        y establece la conexión.
        """

        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database=db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )


    
    
    

    def query_db(self, query, data=None):
        """
        Ejecuta una query SQL.

        SELECT:
            devuelve una lista de diccionarios.

        INSERT:
            devuelve el ID generado.

        UPDATE / DELETE:
            no devuelven records.

        Si ocurre un error:
            devuelve False.
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
    Recibe el nombre de la base de info
    y devuelve una instancia de MySQLConnection.
    """

    return MySQLConnection(db)