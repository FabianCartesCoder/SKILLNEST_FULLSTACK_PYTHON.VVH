import random
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"

# Predicciones para seleccionar al azar
PREDICCIONES = [
    "¡Tendrás un año lleno de viajes, éxito financiero y grandes sorpresas!",
    "Encontrarás una oportunidad inesperada que cambiará tu vida profesional para siempre.",
    "Cuidado: podrías perder tus llaves o derramar café sobre tu camisa favorita esta semana.",
    "Un viejo amigo volverá a tu vida con una noticia increíble.",
    "La suerte no estará de tu lado en los juegos de azar, pero sí en el amor."
]

@app.route("/")
def index():
    """Muestra el formulario principal."""
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    """Procesa el formulario, guarda datos en sesión y elige el destino."""
    session["nombre"] = request.form.get("nombre")
    session["lugar"] = request.form.get("lugar")
    session["numero"] = request.form.get("numero")
    
    # Elegir predicción aleatoria y guardar en sesión
    session["destino"] = random.choice(PREDICCIONES)
    
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    """Muestra la predicción dinámica."""
    if "nombre" not in session:
        return redirect(url_for("index"))
    
    return render_template(
        "futuro.html",
        nombre=session.get("nombre"),
        lugar=session.get("lugar"),
        numero=session.get("numero"),
        destino=session.get("destino")
    )

if __name__ == "__main__":
    app.run(debug=True)