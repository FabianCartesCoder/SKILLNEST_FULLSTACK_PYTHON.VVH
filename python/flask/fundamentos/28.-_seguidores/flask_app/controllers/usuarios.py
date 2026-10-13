from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app.models.usr_data import Usuario
from flask_app.models.seguidor import Seguidor






@app.route("/")
def inicio():
    """
    Redirige la página principal hacia /usr_list.
    """

    return redirect(
        url_for("usr_list")
    )






@app.route("/usr_list")
def usr_list():
    """
    Obtiene todos los usr_list y todas las relaciones.
    """

    lista_usuarios = Usuario.get_all()

    relaciones = Seguidor.get_all()

    return render_template(
        "usr_list.html",
        usr_list=lista_usuarios,
        relaciones=relaciones
    )






@app.route(
    "/usr_list/crear",
    methods=["POST"]
)
def crear_usuario():
    """
    Recibe los info del formulario y crea un usr_data.
    """

    nombre = request.form.get(
        "nombre",
        ""
    ).strip()

    apellido = request.form.get(
        "apellido",
        ""
    ).strip()

    email = request.form.get(
        "email",
        ""
    ).strip()


    if not nombre or not apellido or not email:

        flash(
            "Todos los campos son obligatorios.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    data = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }


    res = Usuario.save(
        data
    )


    if res is False:

        flash(
            "No fue posible crear el usr_data.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    flash(
        "Usuario creado correctamente.",
        "success"
    )


    return redirect(
        url_for("usr_list")
    )






@app.route(
    "/seguir",
    methods=["POST"]
)
def seguir():
    """
    Registra que un usr_data sigue a otro.

    usuario_id:
        usr_data que está siendo seguido.

    seguidor_id:
        usr_data que lo sigue.
    """

    usuario_id_texto = request.form.get(
        "usuario_id"
    )

    seguidor_id_texto = request.form.get(
        "seguidor_id"
    )


    if not usuario_id_texto or not seguidor_id_texto:

        flash(
            "Debes seleccionar un usr_data y un seguidor.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    try:

        usuario_id = int(
            usuario_id_texto
        )

        seguidor_id = int(
            seguidor_id_texto
        )

    except ValueError:

        flash(
            "Los identificadores no son válidos.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    
    
    

    usr_data = Usuario.get_by_id(
        usuario_id
    )


    if usr_data is None:

        flash(
            "El usr_data seleccionado no existe.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    
    
    

    seguidor = Usuario.get_by_id(
        seguidor_id
    )


    if seguidor is None:

        flash(
            "El seguidor seleccionado no existe.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    
    
    

    data = {
        "usuario_id": usuario_id,
        "seguidor_id": seguidor_id
    }


    
    
    

    if Seguidor.existe(data):

        flash(
            "Esta relación ya existe.",
            "warning"
        )

        return redirect(
            url_for("usr_list")
        )


    
    
    

    res = Seguidor.seguir(
        data
    )


    if res is False:

        flash(
            "No fue posible registrar la relación.",
            "danger"
        )

        return redirect(
            url_for("usr_list")
        )


    flash(
        "Relación registrada correctamente.",
        "success"
    )


    return redirect(
        url_for("usr_list")
    )