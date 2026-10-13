from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usr_data import Usuario

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/record")
def record():
    return render_template("record.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    info = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": request.form["password"]
    }

    if not Usuario.validar_usuario(info):
        return redirect("/record")

    if Usuario.existe_email({"email": info["email"]}):
        flash("El email ya está registrado.", "email")
        return redirect("/record")

    password_hash = bcrypt.generate_password_hash(
        info["password"]
    ).decode("utf-8")

    info["password"] = password_hash

    usuario_id = Usuario.guardar(info)

    if not usuario_id:
        flash("No fue posible registrar el usr_data.", "general")
        return redirect("/record")

    session["usuario_id"] = usuario_id

    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    info = {
        "email": request.form["email"].strip().lower(),
        "password": request.form["password"]
    }

    usr_data = Usuario.buscar_por_email({
        "email": info["email"]
    })

    if not usr_data:
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(
        usr_data.password,
        info["password"]
    ):
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")

    session["usuario_id"] = usr_data.id

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "usuario_id" not in session:
        flash("Debes iniciar sesión.", "login")
        return redirect("/")

    usr_data = Usuario.buscar_por_id({
        "id": session["usuario_id"]
    })

    return render_template(
        "dashboard.html",
        usr_data=usr_data
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
