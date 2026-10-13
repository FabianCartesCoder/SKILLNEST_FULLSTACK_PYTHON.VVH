



from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)


from controllers.usr_data import Usuario






app = Flask(__name__)







@app.route("/usr_list")
def usr_list():
    """
    Muestra todos los usr_list.
    """

    todos_los_usuarios = Usuario.get_all()


    return render_template(
        "usr_list.html",
        usr_list=todos_los_usuarios
    )







@app.route("/usr_list/nuevo")
def nuevo_usuario():
    """
    Muestra el formulario para crear un usr_data.
    """

    return render_template(
        "usuario_nuevo.html"
    )







@app.route(
    "/usr_list/crear",
    methods=["POST"]
)
def crear_usuario():
    """
    Recibe y guarda los info del formulario.
    """

    nombre = request.form["nombre"].strip()

    apellido = request.form["apellido"].strip()

    email = request.form["email"].strip()


    if not nombre or not apellido or not email:

        return render_template(
            "usuario_nuevo.html",
            error="Todos los campos son obligatorios."
        )


    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }


    res = Usuario.save(data)


    if res is False:

        return render_template(
            "usuario_nuevo.html",
            error="No fue posible crear el usr_data."
        )


    return redirect(
        url_for("usr_list")
    )







@app.route("/usr_list/<int:id>")
def ver_usuario(id):
    """
    Muestra la información completa de un usr_data.
    """

    usr_data = Usuario.get_by_id(id)


    if usr_data is None:

        return "Usuario no encontrado", 404


    return render_template(
        "usr_data.html",
        usr_data=usr_data
    )







@app.route("/usr_list/editar/<int:id>")
def editar_usuario(id):
    """
    Recupera un usr_data y carga sus info
    dentro del formulario de edición.
    """

    usr_data = Usuario.get_by_id(id)


    if usr_data is None:

        return "Usuario no encontrado", 404


    return render_template(
        "usuario_editar.html",
        usr_data=usr_data
    )







@app.route(
    "/usr_list/<int:id>/actualizar",
    methods=["POST"]
)
def actualizar_usuario(id):
    """
    Recibe los nuevos info y actualiza
    el usr_data correspondiente.
    """

    nombre = request.form["nombre"].strip()

    apellido = request.form["apellido"].strip()

    email = request.form["email"].strip()


    if not nombre or not apellido or not email:

        usr_data = Usuario.get_by_id(id)


        return render_template(
            "usuario_editar.html",
            usr_data=usr_data,
            error="Todos los campos son obligatorios."
        )


    data = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }


    res = Usuario.update(data)


    if res is False:

        usr_data = Usuario.get_by_id(id)


        return render_template(
            "usuario_editar.html",
            usr_data=usr_data,
            error="No fue posible actualizar el usr_data."
        )


    return redirect(
        url_for("usr_list")
    )














@app.route("/usr_list/borrar/<int:id>")
def borrar_usuario(id):
    """
    Elimina el usr_data correspondiente al ID.
    """

    res = Usuario.delete(id)


    if res is False:

        return "No fue posible eliminar el usr_data.", 500


    return redirect(
        url_for("usr_list")
    )






if __name__ == "__main__":

    app.run(debug=True)