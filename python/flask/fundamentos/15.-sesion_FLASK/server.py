from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ==========================================
# RUTA PRINCIPAL (Formulario)
# ==========================================
@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO (POST)
# ==========================================
@app.route("/registrar", methods=["POST"])
def registrar():
    # 1. Obtener los datos del formulario
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    # 2. Imprimir los datos en la terminal
    print("============================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("============================")

    # 3. Redirigir a la ruta GET /resultado usando url_for
    return redirect(url_for("resultado"))


# ==========================================
# MOSTRAR RESULTADO (GET)
# ==========================================
@app.route("/resultado")
def resultado():
    return render_template("resultado.html")


# ==========================================
# RUTA DE AYUDA (Desafío Adicional)
# ==========================================
@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")


if __name__ == "__main__":
    app.run(debug=True)