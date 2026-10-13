from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL


class Pedido:
    """
    Representa un record de la tabla pedidos.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.tipo_arepa = data["tipo_arepa"]
        self.cantidad = data["cantidad"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    
    
    

    @staticmethod
    def validar_pedido(pedido):
        """
        Valida los info recibidos desde el formulario.

        Devuelve:
            True  → información válida.
            False → existen errores.
        """

        es_valido = True


        
        
        

        if not pedido["nombre"]:

            flash(
                "El nombre es obligatorio.",
                "danger"
            )

            es_valido = False


        
        
        

        elif len(pedido["nombre"]) < 2:

            flash(
                "El nombre debe tener al menos 2 caracteres.",
                "danger"
            )

            es_valido = False


        
        
        

        if not pedido["tipo_arepa"]:

            flash(
                "El tipo de arepa es obligatorio.",
                "danger"
            )

            es_valido = False


        
        
        

        if not pedido["cantidad"]:

            flash(
                "La cantidad es obligatoria.",
                "danger"
            )

            es_valido = False

        else:

            
            try:

                cantidad = int(
                    pedido["cantidad"]
                )

                if cantidad <= 0:

                    flash(
                        "La cantidad debe ser mayor que 0.",
                        "danger"
                    )

                    es_valido = False

            except ValueError:

                flash(
                    "La cantidad debe ser mayor que 0.",
                    "danger"
                )

                es_valido = False


        return es_valido


    
    
    

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los pedidos.
        """

        query = """
            SELECT
                id,
                nombre,
                tipo_arepa,
                cantidad,
                created_at,
                updated_at
            FROM pedidos
            ORDER BY id DESC;
        """


        resultados = connectToMySQL(
            "esquema_arepas"
        ).query_db(query)


        pedidos = []


        for pedido in resultados:

            pedidos.append(
                cls(pedido)
            )


        return pedidos


    
    
    

    @classmethod
    def save(cls, data):
        """
        Guarda un nuevo pedido en la base de info.
        """

        query = """
            INSERT INTO pedidos
            (
                nombre,
                tipo_arepa,
                cantidad
            )
            VALUES
            (
                %(nombre)s,
                %(tipo_arepa)s,
                %(cantidad)s
            );
        """


        return connectToMySQL(
            "esquema_arepas"
        ).query_db(
            query,
            data
        )
