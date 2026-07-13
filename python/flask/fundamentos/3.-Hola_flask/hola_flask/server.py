from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "¡Hola Mundo!"

@app.route("/nosotros")
def nosotros():
    return "<h1>¡Conócenos un poco más!</h1>"

#productos
@app.route("/productos")
def productos():
    return "<h1>¡Nuestros productos!</h1>"

#Contacto
@app.route("/contacto")
def contacto():
    return "<h1>¡Contáctanos!</h1>"

if __name__ == "__main__":
    app.run(debug=True)