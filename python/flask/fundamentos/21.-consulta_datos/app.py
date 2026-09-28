# ==========================================================
# SERVIDOR FLASK
# ==========================================================
from flask import Flask, render_template
from mascota import Mascota

# ==========================================================
# CREAR APLICACIÓN
# ==========================================================
app = Flask(__name__)

# ==========================================================
# RUTA PRINCIPAL
# ==========================================================
@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

# ==========================================================
# RUTA PARA BUSCAR MASCOTA POR ID
# ==========================================================
@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca la mascota correspondiente.
    """
    mascota = Mascota.get_by_id(id)

    if mascota is None:
        return "Mascota no encontrada", 404

    return render_template("mascota.html", mascota=mascota)

# ==========================================================
# ACTIVIDAD: RUTA PARA BUSCAR MASCOTA POR NOMBRE
# ==========================================================
@app.route("/mascota/nombre/<string:nombre>")
def mostrar_mascota_por_nombre(nombre):
    """
    Recibe un nombre desde la URL y muestra la mascota correspondiente.
    """
    mascota = Mascota.get_by_name(nombre)

    if mascota is None:
        return f"No se encontró ninguna mascota con el nombre '{nombre}'", 404

    return render_template("mascota.html", mascota=mascota)

# ==========================================================
# DESAFÍO: RUTA PARA FILTRAR MASCOTAS POR TIPO
# ==========================================================
@app.route("/mascotas/tipo/<string:tipo>")
def listar_mascotas_por_tipo(tipo):
    """
    Recibe un tipo desde la URL y muestra el listado de mascotas de ese tipo.
    """
    mascotas = Mascota.get_by_tipo(tipo)

    return render_template("index.html", mascotas=mascotas, tipo_seleccionado=tipo)

# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)