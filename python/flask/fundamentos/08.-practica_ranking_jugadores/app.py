from flask import Flask, render_template
app = Flask(__name__)
jugadores = [

    {
        "nombre": "AlexGamer",
        "puntaje": 5000
    },

    {
        "nombre": "PixelMaster",
        "puntaje": 7500
    },

    {
        "nombre": "ShadowNinja",
        "puntaje": 8200
    },

    {
        "nombre": "CyberWarrior",
        "puntaje": 9100
    },

    {
        "nombre": "UltraNoob",
        "puntaje": 3000
    }

]

@app.route("/ranking")
def ranking():
    return render_template(
        "ranking.html",
        jugadores=jugadores
    )

if __name__ == "__main__":

    app.run(debug=True)