









from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

import random






app = Flask(__name__)

















app.secret_key = "clave-secreta-adivina-numero"






@app.route("/")
def index():
    """
    Muestra la página principal del juego.

    Si todavía no existe un número secreto dentro
    de la sesión, lo generamos aleatoriamente.

    También inicializamos la cantidad de intentos
    y un msg para el usr_data.
    """

    
    
    

    if "numero_secreto" not in session:

        session["numero_secreto"] = random.randint(1, 10)


    
    
    

    if "intentos" not in session:

        session["intentos"] = 0


    
    
    

    if "msg" not in session:

        session["msg"] = (
            "Adivina un número entre 1 y 10."
        )


    
    
    

    if "res" not in session:

        session["res"] = ""


    
    
    

    msg = session["msg"]

    res = session["res"]

    intentos = session["intentos"]


    
    
    

    return render_template(
        "index.html",
        msg=msg,
        res=res,
        intentos=intentos
    )






@app.route("/adivinar", methods=["POST"])
def adivinar():
    """
    Procesa el número ingresado por el usr_data
    y lo compara con el número secreto.
    """

    
    
    

    numero = int(request.form["numero"])


    
    
    

    numero_secreto = session["numero_secreto"]


    
    
    

    session["intentos"] += 1


    
    
    

    if numero < numero_secreto:

        session["msg"] = (
            f"El número secreto es mayor que {numero}."
        )

        session["res"] = "mayor"


    elif numero > numero_secreto:

        session["msg"] = (
            f"El número secreto es menor que {numero}."
        )

        session["res"] = "menor"


    else:

        session["msg"] = (
            f"¡Correcto! El número secreto era {numero_secreto}."
        )

        session["res"] = "correcto"


    
    
    
    
    
    
    
    
    

    return redirect(url_for("index"))






@app.route("/reiniciar")
def reiniciar():
    """
    Elimina la información actual de la sesión
    y redirige al inicio.

    Al volver a "/", se generará un nuevo número secreto.
    """

    
    
    

    session.clear()


    
    
    

    return redirect(url_for("index"))






if __name__ == "__main__":

    app.run(debug=True)