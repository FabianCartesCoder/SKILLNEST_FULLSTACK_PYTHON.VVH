



from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)


from controllers.estudiante import Estudiante






app = Flask(__name__)







@app.route("/estudiantes")
def estudiantes():
    """
    Muestra todos los estudiantes.
    """

    lista_estudiantes = Estudiante.get_all()


    return render_template(
        "estudiantes.html",
        estudiantes=lista_estudiantes
    )







@app.route(
    "/estudiantes/ver/<int:id_estudiante>"
)
def ver_estudiante(id_estudiante):
    """
    Muestra la información de un estudiante específico.
    """

    estudiante = Estudiante.get_by_id(
        id_estudiante
    )


    
    
    

    if estudiante is None:

        return (
            "Estudiante no encontrado",
            404
        )


    return render_template(
        "estudiante_ver.html",
        estudiante=estudiante
    )







@app.route(
    "/estudiantes/editar/<int:id_estudiante>"
)
def editar_estudiante(id_estudiante):
    """
    Recupera un estudiante y muestra
    el formulario de edición.
    """

    estudiante = Estudiante.get_by_id(
        id_estudiante
    )


    if estudiante is None:

        return (
            "Estudiante no encontrado",
            404
        )


    return render_template(
        "estudiante_editar.html",
        estudiante=estudiante
    )







@app.route(
    "/actualizar_estudiante",
    methods=["POST"]
)
def actualizar_estudiante():
    """
    Recibe los info del formulario
    y actualiza el estudiante.
    """

    
    
    

    id_estudiante = request.form[
        "id_estudiante"
    ]

    nombre = request.form[
        "nombre"
    ].strip()

    email = request.form[
        "email"
    ].strip()


    
    
    

    if not nombre or not email:

        estudiante = Estudiante.get_by_id(
            int(id_estudiante)
        )


        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="Todos los campos son obligatorios."
        )


    
    
    

    data = {

        "id_estudiante": id_estudiante,

        "nombre": nombre,

        "email": email

    }


    
    
    

    res = Estudiante.actualizar(
        data
    )


    
    
    

    if res is False:

        estudiante = Estudiante.get_by_id(
            int(id_estudiante)
        )


        return render_template(
            "estudiante_editar.html",
            estudiante=estudiante,
            error="No fue posible actualizar el estudiante."
        )


    
    
    

    return redirect(
        url_for("estudiantes")
    )







@app.route(
    "/eliminar_estudiante/<int:id_estudiante>"
)
def eliminar_estudiante(id_estudiante):
    """
    Elimina un estudiante y vuelve al listado.
    """

    data = {

        "id_estudiante": id_estudiante

    }


    res = Estudiante.eliminar(
        data
    )


    if res is False:

        return (
            "No fue posible eliminar el estudiante.",
            500
        )


    return redirect(
        url_for("estudiantes")
    )






if __name__ == "__main__":

    app.run(debug=True)