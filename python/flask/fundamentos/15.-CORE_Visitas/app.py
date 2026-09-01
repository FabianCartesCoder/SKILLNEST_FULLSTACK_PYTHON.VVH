from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

app = Flask(__name__)

# Clave secreta con un formato distinto
app.config['SECRET_KEY'] = "app-contador-clave-segura-2026"


@app.route("/")
def inicio():
    """Ruta principal para gestionar y mostrar el contador de visitas."""
    
    # Manejo del contador de visitas
    if "contador_visitas" not in session:
        session["contador_visitas"] = 1
    else:
        session["contador_visitas"] += 1

    # Manejo del acumulador de reinicios
    session.setdefault("total_reinicios", 0)

    return render_template(
        "index.html",
        total_visitas=session["contador_visitas"],
        conteo_reinicios=session["total_reinicios"]
    )


@app.route("/incrementar-dos")
def sumar_dos_visitas():
    """Añade 2 unidades al total actual de visitas."""
    session["contador_visitas"] = session.get("contador_visitas", 0) + 2
    return redirect(url_for("inicio"))


@app.route("/resetear")
def resetear_contador():
    """Restablece las visitas a cero e incrementa el contador de reseteos."""
    session["total_reinicios"] = session.get("total_reinicios", 0) + 1
    session["contador_visitas"] = 0
    return redirect(url_for("inicio"))


@app.route("/agregar-cantidad", methods=["POST"])
def agregar_visitas_custom():
    """Suma un valor numérico personalizado recibido desde un formulario."""
    val_ingresado = int(request.form.get("monto", 0))
    session["contador_visitas"] = session.get("contador_visitas", 0) + val_ingresado
    return redirect(url_for("inicio"))


@app.route("/limpiar-sesion")
def borrar_sesion_completa():
    """Borra todos los datos almacenados en la sesión activa."""
    session.clear()
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)