



from flask import Flask, render_template

from controllers.mascota import Mascota






app = Flask(__name__)






@app.route("/")
def index():
    """
    Muestra todas las mascotas.
    """

    mascotas = Mascota.get_all()

    return render_template(
        "index.html",
        mascotas=mascotas
    )



@app.route("/mascota/<string:tipo>")
def mostrar_mascota_tipo(tipo):
    
    mascotas = Mascota.get_by_tipo(tipo)
    
    
    return render_template("mascota.html", mascota=mascotas, tipo=tipo)





@app.route("/mascota/<int:id>")
def mostrar_mascota(id):
    """
    Recibe un ID desde la URL y busca la mascota
    correspondiente en la base de info.
    """

    mascota = Mascota.get_by_id(id)


    
    
    

    if mascota is None:

        return "Mascota no encontrada", 404


    
    
    

    return render_template(
        "mascota.html",
        mascota=mascota
    )








if __name__ == "__main__":

    app.run(debug=True)