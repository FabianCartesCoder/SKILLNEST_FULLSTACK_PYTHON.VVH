from flask_app import app

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_app.models.estudiante import Estudiante
from flask_app.models.curso import Curso
from flask_app.models.inscripcion import Inscripcion






@app.route("/")
def index():
    """
    Muestra el formulario de inscripción.

    También obtiene estudiantes, cursos e inscripciones
    para mostrar información dinámica.
    """

    estudiantes = Estudiante.get_all()

    cursos = Curso.get_all()

    inscripciones = Inscripcion.get_all()


    return render_template(
        "index.html",
        estudiantes=estudiantes,
        cursos=cursos,
        inscripciones=inscripciones
    )






@app.route(
    "/inscribir",
    methods=["POST"]
)
def inscribir():
    """
    Recibe estudiante_id y curso_id y crea
    una relación en la tabla inscripciones.
    """

    estudiante_id_texto = request.form.get(
        "estudiante_id"
    )

    curso_id_texto = request.form.get(
        "curso_id"
    )


    
    
    

    if not estudiante_id_texto or not curso_id_texto:

        flash(
            "Debes seleccionar un estudiante y un curso.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    try:

        estudiante_id = int(
            estudiante_id_texto
        )

        curso_id = int(
            curso_id_texto
        )

    except ValueError:

        flash(
            "Los identificadores no son válidos.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    estudiante = Estudiante.get_by_id(
        estudiante_id
    )


    if estudiante is None:

        flash(
            "El estudiante seleccionado no existe.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    curso = Curso.get_by_id(
        curso_id
    )


    if curso is None:

        flash(
            "El curso seleccionado no existe.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    data = {

        "estudiante_id": estudiante_id,

        "curso_id": curso_id

    }


    
    
    

    if Inscripcion.existe(data):

        flash(
            "El estudiante ya está inscrito en este curso.",
            "warning"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    res = Inscripcion.inscribir_estudiante_en_curso(
        data
    )


    if res is False:

        flash(
            "No fue posible crear la inscripción.",
            "danger"
        )

        return redirect(
            url_for("index")
        )


    
    
    

    flash(
        "Inscripción realizada correctamente.",
        "success"
    )


    return redirect(
        url_for("index")
    )