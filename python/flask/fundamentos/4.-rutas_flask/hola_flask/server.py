from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Rompiendo esquemas</h1><p>Hola, bienvenido a mi primer proyecto con Flask</p>"

@app.route("/exitos")
def exitos():
    return "<h1>Rompiendo esquemas</h1><p>¡Tienes muchos éxitos!</p>"

@app.route("/exito/<nombre>")
def saludo(nombre):
    return f"<h1>Rompiendo esquemas</h1><p>¡Hola, {nombre}!</p>"

@app.route("/color/<nombre>/<color>")
def color(nombre, color):
    return f"<h1>Rompiendo esquemas</h1><p>¡Hola, {nombre}! Tu color favorito es {color}.</p>"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):

    return f"¡Hola {nombre}!" * veces

@app.route("/despedida/<nombre>")
def despedida(nombre):
    return f"<h1>¡Hasta luego, {nombre}! ¡Esperamos verte pronto!</h1>"

@app.route("/presentacion/<nombre>/<int:edad>")
def presentacion(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años."

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return f"La suma es: {a + b}"

@app.route("/multiplicar/<int:a>/<int:b>")
def multiplicar(a, b):
    return f"La multiplicación es: {a * b}"

if __name__ == "__main__":
    app.run(debug=True)