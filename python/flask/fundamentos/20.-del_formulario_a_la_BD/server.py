



from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)


from mascota import Mascota






app = Flask(__name__)







@app.route("/")
def index():
    """
    Recupera todas las mascotas y las envía
    a index.html.
    """

    mascotas = Mascota.get_all()


    return render_template(
        "index.html",
        mascotas=mascotas
    )







@app.route(
    "/crear_mascota",
    methods=["POST"]
)
def crear_mascota():
    """
    Recibe la información del formulario
    y crea una nueva mascota.
    """

    
    
    

    info = {

        "nombre": request.form["nombre"],

        "tipo": request.form["tipo"],

        "color": request.form["color"]

    }


    
    
    

    Mascota.save(info)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    return redirect(
        url_for("index")
    )






if __name__ == "__main__":

    app.run(debug=True)