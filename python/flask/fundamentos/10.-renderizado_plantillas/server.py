from flask import Flask,render_template

app = Flask(__name__)

@app.route("/listas")
def renderizar_listas():

    

    numeros = [7, 15, 22]

    

    listado_estudiantes = [

        {
            "nombre":"Florencia",
            "edad":25
        },

        {
            "nombre":"Valentina",
            "edad":30
        },

        {
            "nombre":"José",
            "edad":27
        },

        {
            "nombre":"Patricio",
            "edad":21
        }

    ]

    return render_template(

        "listas.html",

        numeros=numeros,

        estudiantes=listado_estudiantes

    )

if __name__ == "__main__":

    app.run(debug=True)