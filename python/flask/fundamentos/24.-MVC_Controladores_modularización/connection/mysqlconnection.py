



import pymysql.cursors






class MySQLConnection:
    """
    Administra una conexión con MySQL.
    """

    def __init__(self, db):
        """
        Recibe el nombre de la base de info
        y establece la conexión.
        """

        connection = pymysql.connect(

            host="localhost",

            user="root",

            password="1234",

            database=db,

            charset="utf8mb4",

            cursorclass=pymysql.cursors.DictCursor,

            autocommit=True

        )


        self.connection = connection


    
    
    

    def query_db(
        self,
        query,
        data=None
    ):
        """
        Ejecuta una query SQL.
        """

        with self.connection.cursor() as cursor:

            try:

                
                
                

                query_debug = cursor.mogrify(
                    query,
                    data
                )

                print(
                    "Running Query:",
                    query_debug
                )


                
                
                

                cursor.execute(
                    query,
                    data
                )


                
                
                

                if query.lower().find("insert") >= 0:

                    self.connection.commit()

                    return cursor.lastrowid


                
                
                

                elif query.lower().find("select") >= 0:

                    result = cursor.fetchall()

                    return result


                
                
                

                else:

                    self.connection.commit()


            except Exception as e:

                print(
                    "Something went wrong:",
                    e
                )

                return False


            finally:

                
                
                

                self.connection.close()






def connectToMySQL(db):
    """
    Recibe el nombre de una base de info
    y devuelve una instancia de MySQLConnection.
    """

    return MySQLConnection(db)