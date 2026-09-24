from flask import render_template, request, redirect, url_for, flash
from flask_app import app
from flask_app.models.usuario import Usuario

@app.route("/")
def raiz():
    return redirect(url_for("index_usuarios"))

@app.route("/usuarios")
def index_usuarios():
    todos_los_usuarios = Usuario.obtener_todos()
    return render_template("index.html", usuarios=todos_los_usuarios)

@app.route("/usuarios/nuevo")
def nuevo_usuario():
    return render_template("nuevo.html")

@app.route("/usuarios/crear", methods=["POST"])
def crear_usuario():
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    es_valido, errores = Usuario.validar_datos(datos)

    if not es_valido:
        for err in errores:
            flash(err, "danger")
        return render_template("nuevo.html", datos=datos)

    nuevo_id = Usuario.guardar(datos)
    if nuevo_id:
        flash("¡Usuario creado exitosamente!", "success")
        return redirect(url_for("index_usuarios"))
    
    flash("Ocurrió un problema al guardar en la base de datos.", "danger")
    return render_template("nuevo.html", datos=datos)

@app.route("/usuarios/<int:id>")
def ver_usuario(id):
    usr = Usuario.obtener_por_id(id)
    if not usr:
        flash("El usuario solicitado no existe.", "warning")
        return redirect(url_for("index_usuarios"))
    return render_template("detalle.html", usuario=usr)

@app.route("/usuarios/editar/<int:id>")
def editar_usuario(id):
    usr = Usuario.obtener_por_id(id)
    if not usr:
        flash("Usuario no encontrado.", "warning")
        return redirect(url_for("index_usuarios"))
    return render_template("editar.html", usuario=usr)

@app.route("/usuarios/<int:id>/actualizar", methods=["POST"])
def actualizar_usuario(id):
    datos = {
        "id": id,
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip()
    }

    es_valido, errores = Usuario.validar_datos(datos)

    if not es_valido:
        for err in errores:
            flash(err, "danger")
        usr_temp = Usuario(datos)
        return render_template("editar.html", usuario=usr_temp)

    Usuario.actualizar(datos)
    flash("Información actualizada correctamente.", "success")
    return redirect(url_for("ver_usuario", id=id))

@app.route("/usuarios/borrar/<int:id>")
def borrar_usuario(id):
    Usuario.eliminar(id)
    flash("Usuario eliminado del sistema.", "info")
    return redirect(url_for("index_usuarios"))